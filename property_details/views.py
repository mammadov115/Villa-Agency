from django.shortcuts import render

# Create your views here.

def property_details(request):
    return render(request, "property-details.html")