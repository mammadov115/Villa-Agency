from django.contrib import admin
from django.urls import path, include
from home.views import home
from properties.views import properties
from property_details.views import property_details
from contact_us.views import contact_us

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home_page"),
    path("properties/", properties, name="properties"),
    path("property-details/", property_details, name="property_details"),
    path("contact/", contact_us, name="contact_us" )

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)