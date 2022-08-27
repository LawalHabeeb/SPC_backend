from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.forms import ImageField
from ckeditor.fields import RichTextField
from django_countries.data import COUNTRIES
from datetime import datetime
from . import widgets
#from django.core.validators import 


# Create your models here.

#everything on Event Feature
class EventOrganizer(models.Model):
    organizer_name = models.CharField(max_length=255)
    organizer_website = models.URLField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=15, null=True, blank=True, unique=True)
    Email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.organizer_name

class EventLocation(models.Model):
    CenterName = models.CharField(max_length=255, blank=True)
    FullAddress = models.CharField(max_length=300)
    country = models.CharField(max_length=40, choices= sorted(COUNTRIES.items()))

    def __str__(self):
        return self.CenterName

class Event(models.Model):
    EventName = models.CharField(max_length=250)
    Description = RichTextField(blank=True, null=True)
    FeaturedImage = models.ImageField(upload_to='images', blank=True)
    startdateandtime = models.DateTimeField(default=datetime.now())
    enddateandtime = models.DateTimeField(blank=True, null=True)
    Location = models.ForeignKey(EventLocation, on_delete=models.CASCADE, default=1)
    Organizers = models.ForeignKey(EventOrganizer, on_delete=models.CASCADE, default=1)


#insight class
class Category(models.Model):
    Category = models.CharField(max_length=99)

    def __str__(self):
        return self.Category

class Tags(models.Model):
    tag = models.CharField(max_length=90)

class Insight(models.Model):
    Title = models.CharField(max_length=255)
    InsightDescription = RichTextField(blank=True, null=True)
    InsightImage = models.ImageField(upload_to='insight', blank=True)
    InsightCategory = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    InsightTag = models.ForeignKey(Tags, on_delete=models.CASCADE, default=1)
    WhenPublished = widgets.DateTimeInput(default(datetime.now()))