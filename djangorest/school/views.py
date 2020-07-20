from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Classes, Schools
from django.shortcuts import render, get_object_or_404

def index(request):
    school_list = Schools.objects.order_by()
    context = {'school_list': school_list}
    return render(request, 'school/index.html', context)


def class_list(request, school_id):
    try:
        school = get_object_or_404(Schools, pk=school_id)
        return render(request, 'school/classes.html', {'school': school})
    except:
        return render(request, 'school/404.html')


def student_list(request, class_id, school_id):
    classes = get_object_or_404(Classes, pk=class_id)
    school = get_object_or_404(Schools, pk=school_id)
    return render(request, 'school/students.html', {'classes': classes})

def welcome(request, name):
    reponse = ("Xin chao %s.")
    return HttpResponse( reponse % name)