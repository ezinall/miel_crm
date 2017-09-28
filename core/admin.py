from django.contrib import admin

# Register your models here.

from . import models
from django.contrib import admin


admin.site.register(models.User)
