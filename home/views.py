from django.shortcuts import render

# Create your views here.

def home(request):
    is_home_page = True
    return render(request, "index.html", locals())
