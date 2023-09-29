from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
# Register your models here.

class SocialLinkInline(admin.StackedInline):
    model = SocialMediaLink
    extra = 1    

@admin.register(HeaderData)
class HeaderDataAdmin(admin.ModelAdmin):
    model = HeaderData
    inlines = [SocialLinkInline]

    def has_add_permission(self, request: HttpRequest) -> bool:
        objects = HeaderData.objects.all().count()
        return True if objects == 0 else False
    
    def render_change_form(self, request: Any, context: Any, add: bool = ..., change: bool = ..., form_url: str = ..., obj: Any | None = ...) -> Any:
        context.update({
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ['location', 'text']