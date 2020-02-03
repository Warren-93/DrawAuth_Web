from django.db import models


# Create your models here.

class DrawAuth_userIcons(models.Model):
    Icon_Images = models.ImageField(upload_to="images/UserIcons")
    Icon_Used = models.BooleanField(default="n")


class DrawAuth_user(models.Model):
    UserIcon = models.ImageField()
    AuthDrawing_One = models.ImageField(upload_to="static/images/UserDrawings")
    AuthDrawing_Two = models.ImageField(upload_to="static/images/UserDrawings")
    AuthDrawing_Three = models.ImageField(upload_to="static/images/UserDrawings")
    AuthDrawing_Four = models.ImageField(upload_to="static/images/UserDrawings")


class DrawAuth_testImages(models.Model):
    DrawAuth_ImageName = models.ImageField(upload_to="static/images/TestImages")
