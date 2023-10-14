from django.shortcuts import render
from .models import Slider, Video, FunFacts, Contact, HeaderData

from .forms import MessageForm

import re

# Create your views here.

def home(request):

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        
    is_home_page = True
    slides = Slider.objects.all()
    video_section = Video.objects.first()
    fun_facts = FunFacts.objects.first()
    contact_section = Contact.objects.first()
    phone_number = HeaderData.objects.first().number
    # map link
    map_link = contact_section.map_link
    src_match = re.search(r'src="([^"]+)"', map_link)
    # form
    form = MessageForm()
    
    if src_match:
        map_link = src_match.group(1)
        print(map_link)
    
    return render(request, "index.html", locals())
