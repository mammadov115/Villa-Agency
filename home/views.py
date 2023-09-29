from django.shortcuts import render
from .models import Slider

# Create your views here.

def home(request):
    is_home_page = True
    slides = Slider.objects.all()
    return render(request, "index.html", locals())
