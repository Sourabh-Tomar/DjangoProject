from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('me collage wala hu')

def collagehtml(request):
    return render(request,'collage/index.html')
