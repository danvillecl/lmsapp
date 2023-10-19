from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import permissions
from . import models
from . import serializers
from rest_framework import generics

# Serializer for Instuctor Models
class IntructorList(generics.ListCreateAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.IntructorSerailizer

class InstructorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.IntructorSerailizer

# for student
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# for Category Serializer
class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

# Views for Course Model
class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

# Views for Enrosllments Model
class EnrollmentList(generics.ListCreateAPIView):
    queryset = models.Enrollments.objects.all()
    serializer_class = serializers.EnrollmentSerializer

class EnrollmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Enrollments.objects.all()
    serializer_class = serializers.EnrollmentSerializer

# Views for Syllabus
class SyllabusList(generics.ListCreateAPIView):
    queryset = models.Syllabus.objects.all()
    serializer_class = serializers.SyllabusSerializer

class SyllabusDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Syllabus.objects.all()
    serializer_class = serializers.SyllabusSerializer

# Views for Content
class ContentList(generics.ListCreateAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer

class ContentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer

# Views for Materials
class MaterialList(generics.ListCreateAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer

class MaterialDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer

# Views for Faq
class FaqList(generics.ListCreateAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerialzer

class FaqDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerialzer

# Views for ClassSchedule
class ClassScheduleList(generics.ListCreateAPIView):
    queryset = models.ClassSchedule.objects.all()
    serializer_class = serializers.ClassScheduleSerializer

class ClassScheduleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClassSchedule.objects.all()
    serializer_class = serializers.ClassScheduleSerializer

# Views for QuizQAndA
# class QuizQAndAList(generics.ListCreateAPIView):
#     queryset = models.QuizQAndA.objects.all()
#     serializer_class = serializers.QuizQAndASerializer

# class QuizQAndADetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.QuizQAndA.objects.all()
#     serializer_class = serializers.QuizQAndASerializer

# # Views for QuizQAndA
# class QuizesList(generics.ListCreateAPIView):
#     queryset = models.Quizes.objects.all()
#     serializer_class = serializers.QuizesSerializer

class QuizesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quizes.objects.all()
    serializer_class = serializers.QuizesSerializer

# def instructor_login (request):
#     email=request.POST['email']
#     password = request.POST['password']
#     instructorData=models.Instructor.objects.get(email=email,password=password)
#     if instructorData:
#         return JsonResponse({'bool':True})
#     else:
#         return JsonResponse({'bool':False})

def instructor_login (request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    instructorData = models.Instructor.objects.filter(email=email, password=password)
    if instructorData.exists():
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})
