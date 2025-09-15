from django.http import HttpResponse, HttpResponseRedirect
#browser pe render karane ke liye only text content
from django.shortcuts import render
# for displaying template file 
from service.models import Service

def home(request):
  data = {
    'title': 'Home page',
    'pageName': 'Home Page',
    'clist': ['python', 'javascript', 'java'],
    'numbers': [],
    'student_details': [
      {'name':'nikhil verma', 'phonenum':888888888},
      {'name':'mohit kumar',  'phonenum':777777777},
    ]
  }
  return render(request, "index.html", data)

def aboutUS(request):
  return HttpResponse("<h1>This is about us page</h1>")

def courses(request):
  return HttpResponse("<h1>This is avaliable courses</h1>")

def allCourses(request, courseId):
  return HttpResponse(courseId)

def index1(request):
  return render(request, "index1.html")

def web(request):
  return render(request, "home.html")

def formGet(request):
    output = None
    try:
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        output = n1+n2
        # print(n1+n2)
    except:
        pass

    return render(request, "formGet.html", {'ans':output})

def formPost(request):
    output = None
    try:
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        output = n1+n2
        # print(n1+n2)
    except:
        pass

    return render(request, "formPost.html", {'ans':output})