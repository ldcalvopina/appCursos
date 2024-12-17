# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Courses, Student
from .serializer import StudentSerializer, CourseSerializer

class CourseViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer