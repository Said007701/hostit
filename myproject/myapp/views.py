from django.shortcuts import render,redirect,get_object_or_404
from .models import index1
from . forms import index1Form

# crud 1
def list(request):
    obj = index1.objects.all()
    return render(request,'list.html', {'obj':obj})

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
    obj = index1.objects.get(id=id)
    if request.method == "POST":
        form = index1Form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = index1Form(instance=obj)
    return render(request, 'update.html', {'form':form})

def index1_delete(request, id):
    obj = get_object_or_404(index1, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('list')
    return render(request, 'delete.html', {'obj': obj})

def creat(request):
    return render(request, 'create.html')

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')

def index(request): 
    obj = index1.objects.all()
    return render(request, 'index.html',{'obj':obj})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def price(request):
    return render(request, 'price.html')

def service(request):
    return render(request, 'service.html')

    