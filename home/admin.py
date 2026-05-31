from django.contrib import admin
from .models import *

# HOME MODULE

admin.site.register(Banner)
admin.site.register(VisionMission)
admin.site.register(Statistic)
admin.site.register(Initiative)

# ABOUT US MODULE

admin.site.register(OurStory)
admin.site.register(CoreValue)
admin.site.register(Program)
admin.site.register(TeamMember)

# PROJECT MODULE

admin.site.register(Project)

# MEDIA MODULE

admin.site.register(PressRelease)
admin.site.register(MediaCoverage)
admin.site.register(ImageGallery)
admin.site.register(Video)