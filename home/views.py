from django.shortcuts import render
from .models import *

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


def projects(request):
    status = request.GET.get('status')

    if status:
        projects = Project.objects.filter(status=status)
    else:
        projects = Project.objects.all()

    return render(request, 'project.html', {
        'projects': projects
    })