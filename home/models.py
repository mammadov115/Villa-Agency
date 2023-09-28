from django.db import models

# Create your models here.

class HeaderData(models.Model):        
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
    

