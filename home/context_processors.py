from .models import HeaderData, SocialMediaLink

def data(request):
    data = HeaderData.objects.first()
    platform_list = {i.platform: i.link for i in SocialMediaLink.objects.all()}
    return locals()