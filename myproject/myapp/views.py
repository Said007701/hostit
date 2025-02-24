from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
# from .serializers import UserContactSerializer
from rest_framework.permissions import AllowAny


from .models import index1,index2
from . forms import index1Form,index2Form

# crud 1
def list(request):
    crud1 = index1.objects.all()
    return render(request,'list.html', {'crud1':crud1})

def index1_create(request):
    if request.method == "POST":
        form = index1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = index1Form()

    return render(request, 'create.html',{'form':form})

def index1_update(request, id):
    crud1 = index1.objects.get(id=id)
    if request.method == "POST":
        form = index1Form(request.POST, instance=crud1)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = index1Form(instance=crud1)
    return render(request, 'update.html', {'form':form})

def index1_delete(request, id):
    crud1 = get_object_or_404(index1, id=id)
    if request.method == "POST":
        crud1.delete()
        return redirect('list')
    return render(request, 'delete.html', {'crud1': crud1})

def creat(request):
    return render(request, 'create.html')

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')

def index(request): 
    crud1 = index1.objects.all()
    kluch={
        'crud1': crud1
    }
    return render(request, 'index.html',{'kluch':kluch})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def price(request):
    return render(request, 'price.html')

def service(request):
    return render(request, 'service.html')

    