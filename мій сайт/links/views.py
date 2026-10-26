from django.shortcuts import render

from .models import ProfileLink, SiteProfile


def home(request):
    profile = SiteProfile.get_profile()
    links = ProfileLink.objects.filter(profile=profile, is_active=True)
    return render(request, "links/home.html", {"profile": profile, "links": links})
