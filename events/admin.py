from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.EventOrganizer, models.EventLocation, models.Event)
admin.site.register(models.Category, models.Tags, models.Insight)