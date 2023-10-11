from django.db import models

# Create your models here.

class HeaderData(models.Model): 
    logo = models.CharField(max_length=150)       
    email = models.EmailField()
    location = models.CharField(max_length=250)

    def __str__(self):
        return "Header Info"

class SocialMediaLink(models.Model):
    class SocialMediaAccount(models.TextChoices):
        FB = "Facebook", "Facebook"
        TW = "Twitter", "Twitter"
        IN = "LinkedIn", "LinkedIn"
        IG = "Instagram", "Instagram"

    header_data = models.ForeignKey(HeaderData, on_delete=models.CASCADE, related_name="social_media_links")
    platform = models.CharField(max_length=50, choices=SocialMediaAccount.choices)
    link = models.URLField()


    def __str__(self):
        return self.platform

# slider
class Slider(models.Model):
    image = models.ImageField(upload_to="Slider Images/%Y-%m-%d")
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    text = models.TextField(max_length=500)


    def __str__(self):
        return f'{self.country} - {self.text}'
    
# video section
    
class Video(models.Model):
    background_image = models.ImageField(upload_to="Video Section/Background Images/%Y-%m-%d")
    text = models.CharField(max_length=150)
    video_thumbnail = models.ImageField(upload_to="Video Section/Thumbnail Images/%Y-%m-%d")
    link = models.URLField()

    def __str__(self):
        return "Video Section"
    
    
