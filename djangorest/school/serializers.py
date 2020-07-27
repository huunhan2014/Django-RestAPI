from rest_framework import serializers
from .models import Students, Classes, Schools


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name_student', 'classes']


