from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.title

class Student(models.Model):
    courses = models.ManyToManyField(Courses, related_name='students')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    