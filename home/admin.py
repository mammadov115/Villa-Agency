from django.contrib import admin
from .models import *
# Register your models here.

class SocialLinkInline(admin.StackedInline):
    model = SocialMediaLink
    extra = 1    

@admin.register(HeaderData)
class HeaderDataAdmin(admin.ModelAdmin):
    model = HeaderData
    inlines = [SocialLinkInline]
