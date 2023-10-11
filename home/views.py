from django.shortcuts import render
from .models import Slider, Video, FunFacts

# Create your views here.

def home(request):
    is_home_page = True
    slides = Slider.objects.all()
    video_section = Video.objects.first()
    fun_facts = FunFacts.objects.first()
    return render(request, "index.html", locals())
