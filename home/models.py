from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

# Create your models here.

phone_number_validator = RegexValidator(r'[-+()\d]+', "Wrong phone number!") 

class HeaderData(models.Model): 
    logo = models.CharField(max_length=150)       
    email = models.EmailField()
    number = models.CharField(max_length=50, validators=[phone_number_validator], verbose_name="Phone Number", help_text="Enter your phone number")
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
    
#  Fun facts section
class FunFacts(models.Model):
    buildings_finished = models.PositiveIntegerField()
    years_experience = models.PositiveIntegerField()
    awards_won_date = models.PositiveBigIntegerField(help_text="Enter awards won year:")
    awards_won = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Fun Facts"
        verbose_name_plural = "Fun Facts"

    def __str__(self) -> str:
        return "Fun facts section"

# Contact us section
class Contact(models.Model):
    bg_image = models.ImageField()
    text = models.CharField(max_length=250)
    map_link = models.TextField(help_text="Enter Google Map location embed code")

    def __str__(self):
        return "Contact Us section"
    
# Message
class Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Footer
class Footer(models.Model):
    footer_text = RichTextField(config_name='awesome_ckeditor')

    def __str__(self):
        return "Footer info"
    
    class Meta:
        verbose_name_plural = "Footer Section"
    