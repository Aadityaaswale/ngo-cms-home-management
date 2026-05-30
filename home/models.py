from django.db import models

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