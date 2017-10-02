from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect

from app_flat.models.flat_usage import Flat, FlatStatus


def flat_view(request, entity_id):
    flat = get_object_or_404(Flat, id=entity_id)
    context = {'flat': flat}
    return render(request, 'core/flat_view.html', context=context)


def set_status(request, entity_id, status_id):
    flat = get_object_or_404(Flat, id=entity_id)
    flat.status = get_object_or_404(FlatStatus, id=status_id)
    flat.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
