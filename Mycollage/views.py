from django.shortcuts import render
from django.http import HttpResponse
from collage.models import Collage

def learn_django(request):
    return HttpResponse('me main wala pagal hu')
def mycollagehtml(request):
    return render(request,'index.html')
def collageshow(request):
    col= Collage.objects.all()
    params = {'coldata':col}
    return render(request,'collegeshow.html',params)

