from django.db import models


# HOME MODULE

class Banner(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')
    order = models.IntegerField(default=1)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class VisionMission(models.Model):
    vision_title = models.CharField(max_length=150)
    vision_description = models.TextField()
    mission_title = models.CharField(max_length=150)
    mission_description = models.TextField()

    def __str__(self):
        return "Vision & Mission"


class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    order = models.IntegerField(default=1)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class Initiative(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='initiatives/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# ABOUT US MODULE

class OurStory(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Our Story"


class CoreValue(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name


# PROJECT MODULE

class Project(models.Model):

    STATUS_CHOICES = (
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Upcoming', 'Upcoming'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title


# MEDIA MODULE

class PressRelease(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title


class MediaCoverage(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description if self.description else "Gallery Image"


class Video(models.Model):
    video_url = models.URLField()
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description if self.description else "Video"