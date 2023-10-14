from .models import HeaderData, SocialMediaLink, Footer

def data(request):
    data = HeaderData.objects.first()
    platform_list = {i.platform: i.link for i in SocialMediaLink.objects.all()}
    return locals()

def footer(request):
    footer_info_text = Footer.objects.first().footer_text
    return locals()