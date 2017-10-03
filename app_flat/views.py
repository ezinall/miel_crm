from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models.flat_usage import FlatUsage, FlatStatus
from .forms import FlatUsageForm


@login_required(login_url='core:login')
def flat_new(request):
    context = {'form': FlatUsageForm}
    return render(request, 'core/flat_new.html', context=context)


@login_required(login_url='core:login')
def flat_view(request, entity_id):
    flat = get_object_or_404(FlatUsage, id=entity_id)
    context = {'flat': flat}
    return render(request, 'core/flat_view.html', context=context)


@login_required(login_url='core:login')
def set_status(request, entity_id, status_id):
    flat = get_object_or_404(FlatUsage, id=entity_id)
    flat.status = get_object_or_404(FlatStatus, id=status_id)
    flat.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
