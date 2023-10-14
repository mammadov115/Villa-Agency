from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    

class Location(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Property(models.Model):
    image = models.ImageField(upload_to="Property Images/%Y/%m/%d", null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cost = models.BigIntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    number_of_rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField(verbose_name="Area(m²):")
    floor = models.IntegerField()
    parking_available = models.BooleanField()
    parking = models.IntegerField(verbose_name="Parking(spots)", null=True)
    contract = models.CharField(max_length=250)
    payment = models.CharField(max_length=250)
    safety = models.CharField(max_length=250)
    description = RichTextField()

    def __str__(self):
        return f'No category' if self.category == None else self.category.name
    
    class Meta:
        verbose_name_plural = "Properties"
        

class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = RichTextField()

    def __str__(self):
        return self.question

    
