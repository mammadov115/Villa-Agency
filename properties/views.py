from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def properties(request):
    categories = Category.objects.all()
    properties_list = Property.objects.all()
    paginator = Paginator(properties_list, 12)
    page_number = request.GET.get('page', 1)
    properties = paginator.page(page_number)
    return render(request, "properties.html", locals())