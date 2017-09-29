from django.shortcuts import render, redirect

# Create your views here

from app_cbase.models.apartment_sec import Apartment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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
                pass
        else:
            pass
    else:
        return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login/')
def index_view(request):
    return render(request, 'core/index.html')


@login_required(login_url='login/')
def objects_view(request):
    objects = Apartment.objects.all()
    context = {'objects': objects}
    return render(request, 'core/objects.html', context=context)
