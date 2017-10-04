# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from .models import Profile, GroupHead, UserPositionType, Task, TaskComments, Client


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Допольнительно'


class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )


class GroupInline(admin.StackedInline):
    model = GroupHead
    can_delete = False
    verbose_name_plural = 'Руководитель'


class GroupAdmin(GroupAdmin):
    inlines = (GroupInline, )


class TaskCommentsInline(admin.StackedInline):
    model = TaskComments
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    inlines = (TaskCommentsInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register([UserPositionType, Client])
