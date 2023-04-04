from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def aboutPage(request):
    return render(request,'about.html')

def contactPage(request):
    return render(request,'contact.html')

def servicePage(request):
    return render(request,'service.html')

def helloWorld(request):
   return HttpResponse('This is world')