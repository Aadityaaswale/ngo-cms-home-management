from django.shortcuts import render
from .models import *


# HOME PAGE

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


# ABOUT PAGE

def about(request):
    story = OurStory.objects.first()
    values = CoreValue.objects.all()
    programs = Program.objects.all()
    team = TeamMember.objects.all()

    context = {
        'story': story,
        'values': values,
        'programs': programs,
        'team': team,
    }

    return render(request, 'about.html', context)


# PROJECT PAGE

def projects(request):

    status = request.GET.get('status')

    if status:
        project_list = Project.objects.filter(status=status)
    else:
        project_list = Project.objects.all()

    context = {
        'projects': project_list,
    }

    return render(request, 'project.html', context)


# MEDIA PAGE

def media(request):

    press_releases = PressRelease.objects.all()
    media_coverages = MediaCoverage.objects.all()
    gallery_images = ImageGallery.objects.all()
    videos = Video.objects.all()

    context = {
        'press_releases': press_releases,
        'media_coverages': media_coverages,
        'gallery_images': gallery_images,
        'videos': videos,
    }

    return render(request, 'media.html', context)