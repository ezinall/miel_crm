# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


class EmployeeInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Допольнительно'


class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
