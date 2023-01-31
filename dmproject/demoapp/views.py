from django.http import HttpResponse
from django.shortcuts import render
from .models import Fruit, Person

def demo(request):
    obj=Fruit.objects.all()
    obj1 =Person.objects.all()
    return render(request,"index.html",{'result':obj,'new':obj1})
