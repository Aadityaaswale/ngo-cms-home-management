from django.shortcuts import render
from .models import Banner, VisionMission, Statistic, Initiative

def home(request):
    banners = Banner.objects.filter(status=True)
    vision_mission = VisionMission.objects.first()
    statistics = Statistic.objects.filter(status=True)
    initiatives = Initiative.objects.filter(status=True)

    context = {
        'banners': banners,
        'vision_mission': vision_mission,
        'statistics': statistics,
        'initiatives': initiatives,
    }

    return render(request, 'home.html', context)