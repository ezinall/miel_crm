from django.shortcuts import render, redirect, get_object_or_404

# Create your views here

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db.models import Q

from datetime import date

from app_flat.models import FlatUsage, FlatStatus
from .models import Task, Client, TaskExecutor
from .forms import TaskExecutorForm, TaskForm, TaskCommentForm


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


@login_required(login_url='core:login')
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='core:login')
def index_view(request):
    return render(request, 'core/index.html')


@login_required(login_url='core:login')
def panel_view(request):
    context = {}
    taskexecutor = TaskExecutor.objects.filter(executor=request.user).values_list('task_id', flat=True)
    context['flats'] = FlatUsage.objects.filter(major=request.user)
    context['tasks'] = Task.objects.filter(Q(id__in=taskexecutor) | Q(director=request.user)).order_by('-priority')
    context['statuses'] = FlatStatus.objects.all()
    context['users'] = User.objects.all()
    context['task_form'] = TaskForm
    context['task_executor_form'] = TaskExecutorForm
    context['task_comment_form'] = TaskCommentForm
    context['date_now'] = date.today()
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
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.director = User.objects.get(id=request.user.id)
            task.save()
            for user_id in request.POST.getlist('user_id'):
                form = TaskExecutorForm()
                taskexecutor = form.save(commit=False)
                taskexecutor.task = get_object_or_404(Task, id=task.id)
                taskexecutor.executor = get_object_or_404(User, id=int(user_id))
                taskexecutor.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='core:login')
def task_postpone(request, task_id, date):
    task = get_object_or_404(Task, id=task_id)
    task.deadline = date
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='core:login')
def task_done(request, task_id):
    taskexecutor = get_object_or_404(TaskExecutor, task=task_id, executor=request.user)
    taskexecutor.done = True
    taskexecutor.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='core:login')
def task_del(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.active = False
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='core:login')
def task_add_comment(request, task_id):
    if request.POST:
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = get_object_or_404(Task, id=task_id)
            comment.author = User.objects.get(id=request.user.id)
            comment.save()
        else:
            form = TaskCommentForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
