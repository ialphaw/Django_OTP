from django.contrib import admin
from . import models


class Admin(admin.ModelAdmin):
    list_display = ('__str__', 'authorized',)

admin.site.register(models.Driver, Admin)
admin.site.register(models.Passenger)
