from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('student without render')

def studentwala(request):
    return render(request,'students/index.html')

