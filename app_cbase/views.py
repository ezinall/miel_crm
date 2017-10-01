from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect

from app_cbase.models.apartment_sec import Apartment, StatusType


def set_status(request, apartment_id, status_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    apartment.status = get_object_or_404(StatusType, id=status_id)
    apartment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
