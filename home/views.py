from django.shortcuts import render
from .models import Slider, Video

# Create your views here.

def home(request):
    is_home_page = True
    slides = Slider.objects.all()
    video_section = Video.objects.first()
    return render(request, "index.html", locals())
