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
        objects = HeaderData.objects.count()
        return True if objects == 0 else False
    
    def render_change_form(self, request: Any, context: Any, add: bool = ..., change: bool = ..., form_url: str = ..., obj: Any | None = ...) -> Any:
        context.update({
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ['country', 'text']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    model = Video

    def has_add_permission(self, request: HttpRequest) -> bool:
        objects = Video.objects.count()
        return True if objects == 0 else False

    def render_change_form(self, request: Any, context: Any, add: bool = ..., change: bool = ..., form_url: str = ..., obj: Any | None = ...) -> Any:
        context.update({
            'show_save_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    

@admin.register(FunFacts)
class FunFactsAdmin(admin.ModelAdmin):
    model = FunFacts
    
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        objects = FunFacts.objects.count()
        return True if objects == 0 else False
    
    def changeform_view(self, request: HttpRequest, object_id: str | None = ..., form_url: str = ..., extra_context: dict[str, bool] | None = ...) -> Any:
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact

    def has_add_permission(self, request: HttpRequest) -> bool:
        objects = Contact.objects.count()
        return True if objects==0 else False

    def changeform_view(self, request: HttpRequest, object_id: str | None = ..., form_url: str = ..., extra_context: dict[str, bool] | None = ...) -> Any:
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ["name", "email", "subject", "date"]
    
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    model = Footer

    def has_add_permission(self, request: HttpRequest) -> bool:
        is_empty = Footer.objects.count() == 0
        return True if is_empty else False

    def changeform_view(self, request: HttpRequest, object_id: str | None = ..., form_url: str = ..., extra_context: dict[str, bool] | None = ...) -> Any:
        extra_context = extra_context or {}
        extra_context["show_save_and_add_another"] = False
        return super().changeform_view(request, object_id, form_url, extra_context)