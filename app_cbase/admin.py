from django.contrib import admin

# Register your models here.

from .models import *


class ImagesInline(admin.StackedInline):
    model = ImageApartment
    extra = 1


class CommentsInline(admin.StackedInline):
    model = CommentApartment
    extra = 1
    readonly_fields = ['date_pub']


class ApartmentSecAdmin(admin.ModelAdmin):
    list_display = ['name', 'major']
    readonly_fields = ['date_pub', 'date_change']
    inlines = [ImagesInline, CommentsInline]
    fieldsets = (
        (None, {
            'fields': (
                ('owner', 'date_start'),
                'app_type', 'cadastral',
                ('rooms', 'apartments', 'penthouse'),
                'total_area',
                ('floor', 'floors'),
                'rooms_area',
                'living_area',
                'kitchen_area',
                ('loggia', 'balcony'),
                ('windows_yard', 'windows_street'),
                ('separate_bath', 'combine_bath'),
                'repairs',
                'phone',
                'name_place',
                'year',
                ('house_type', 'house_ver'),
                'ceiling',
                ('pas_lift', 'ser_lift'),
                'ramp',
                'chute',
                'parking',
                'video',
                'info',
                ('prise', 'prise_type', 'mortgage'),
                'sale_type',
                'bonus',
                ('major', 'comm', 'comm_type'),
                ('date_pub', 'date_change'),
                'name',
                ('active', 'calls', 'views', 'status'),
            )
        }),
    )


admin.site.register(Apartment, ApartmentSecAdmin)
