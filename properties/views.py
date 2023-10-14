from django.shortcuts import render
from .models import *
# Create your views here.

def properties(request):
    categories = Category.objects.all()
    properties = Property.objects.all()
    return render(request, "properties.html", locals())