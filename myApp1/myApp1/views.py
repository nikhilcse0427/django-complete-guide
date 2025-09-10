from django.http import HttpResponse 
#browser pe render karane ke liye only text content
from django.shortcuts import render
# for displaying template file 

def home(request):
  data = {
    'title': 'Home page',
    'pageName': 'Home Page',
  }
  return render(request, "index.html", data)

def aboutUS(request):
  return HttpResponse("<h1>This is about us page</h1>")

def courses(request):
  return HttpResponse("<h1>This is avaliable courses</h1>")

def allCourses(request, courseId):
  return HttpResponse(courseId)

