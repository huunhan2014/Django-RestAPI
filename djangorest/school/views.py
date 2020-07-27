from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from .models import Schools, Students, Classes
from rest_framework import permissions
from .serializers import SchoolSerializer, ClassSerializer, StudentSerializer

from .models import Classes, Schools
from django.shortcuts import render, get_object_or_404
import random

def index(request):
    school_list = Schools.objects.order_by()
    context = {'school_list': school_list}
    return render(request, 'school/index.html', context)

def index_class(request):
    class_list = Classes.objects.all()
    data_output = []
    for c in class_list:
        data_output.append({'name': c.name_class, 'grade': c.grade})
    context = {'class_list': data_output}
    return JsonResponse(context)

def put_class(request):
    try:
        data = request.data
        c = Classes.objects.create(name_class=re, grade=random.randint(0, 12))
        c.save()
        return JsonResponse({'status': 200})
    except Exception as e:
        return JsonResponse({'status': 404, 'message': e})

def class_detail(request, class_id):
    try:
        c = get_object_or_404(Classes, pk=class_id)
        return JsonResponse({'status': 200, 'data': {'name': c.name_class, 'grade': c.grade}})
    except Exception as e:
        return JsonResponse({'status': 404, 'message': e})


def class_list(request, school_id):
    try:
        school = get_object_or_404(Schools, pk=school_id)
        return render(request, 'school/classes.html', {'school': school})
    except:
        return render(request, 'school/404.html')


def student_list(request, class_id, school_id):
    classes = get_object_or_404(Classes, pk=class_id)
    return render(request, 'school/students.html', {'classes': classes})


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class ClassView(views.APIView):
    def post(self, request):
        name = request.query_params['name']
        grade = request.query_params['grade']
        try:
            data = request.data
            c = Classes.objects.create(name_class=name, grade=int(grade))
            c.save()
            return JsonResponse({'status': 200})
        except Exception as e:
            return JsonResponse({'status': 404, 'message': e})