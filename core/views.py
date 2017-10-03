from django.shortcuts import render, redirect

# Create your views here

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from app_flat.models import FlatUsage, FlatStatus
from .forms import TaskForm


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                context = {'noactive': True}
                return render(request, 'core/login.html', context=context)
        else:
            context = {'error': True}
            return render(request, 'core/login.html', context=context)
    else:
        return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='core:login')
def index_view(request):
    return render(request, 'core/index.html')


@login_required(login_url='core:login')
def panel_view(request):
    if request.POST:
        pass
    context = {}
    all_flats = FlatUsage.objects.all()
    context['flats'] = all_flats.filter(major=request.user)
    context['statuses'] = FlatStatus.objects.all()
    context['form'] = TaskForm
    return render(request, 'core/panel.html', context=context)


@login_required(login_url='core:login')
def objects_view(request):
    all_objects = FlatUsage.objects.all()
    objects = all_objects.filter(major=None)
    context = {'objects': objects}
    return render(request, 'core/objects.html', context=context)


@login_required(login_url='core:login')
def calendar_view(request):
    return render(request, 'core/calendar.html')


@login_required(login_url='core:login')
def news_view(request):
    return render(request, 'core/news.html')


@login_required(login_url='core:login')
def docs_view(request):
    return render(request, 'core/docs.html')


@login_required(login_url='core:login')
def contacts_view(request):
    return render(request, 'core/contacts.html')


@login_required(login_url='core:login')
def profile_view(request):
    return render(request, 'core/profile.html')


@login_required(login_url='core:login')
def task_new(request):
    if request.POST:
        print('HHHHAAAAAAAAAAAA')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        pass
