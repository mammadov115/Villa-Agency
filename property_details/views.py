from django.shortcuts import render
from properties.models import Property
# Create your views here.

def property_details(request, category, location, id):
    property = Property.objects.get(id=id)


    return render(request, "property-details.html", locals())