from django.shortcuts import HttpResponse, HttpResponseRedirect, render

# Create your views here.

def index(request):
    return render(request, "mysite/index.html")

def hobbies(request):
    return render(request, "mysite/hobbies.html")

def projects(request):
    return render(request, "mysite/project.html")