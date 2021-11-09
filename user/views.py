from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile


def index(request):
    if request.user.is_authenticated:
        return redirect('profile:profile')
    template = 'index.html'
    context = {}
    return render(request, template, context)


def login_page(request):
    page_type = 'login'
    template = 'registration_login.html'
    context = {
        'page_type': page_type,
    }
    if request.user.is_authenticated:
        return redirect('profile:profile')
    if request.method != 'POST':
        return render(request, template, context)
    username = request.POST['username'].lower()
    password = request.POST['password']
    try:
        user = User.objects.get(username=username)
    except:
        messages.error(request, 'Пользователь не найден')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile:profile')
    else:
        messages.error(request, 'Имя пользователя или пароль указаны неверно')


def user_profile_create(request):
    template = 'registration_login.html'
    page_type = 'registration'
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        messages.success(request, 'Профиль был успешно создан')
        login(request, user)
        return redirect('profile:profile_edit')
    else:
        messages.error(request, 'Проверьте введённые данные')
    context = {
        'form': form,
        'page_type': page_type,
    }
    return render(request, template, context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'Вы вышли из профиля')
    return redirect('index:index')


@login_required(login_url='profile:login')
def profile(request):
    template = 'profile_page.html'
    profile = request.user.profile
    ipitems = profile.ipitem_set.all()
    context = {
        'profile': profile,
        'ipitems': ipitems,
    }
    return render(request, template, context)


@login_required(login_url='profile:login')
def profile_edit(request):
    template = 'profile_form.html'
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile:profile')
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required(login_url='profile:login')
def profile_delete(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.user.profile != profile:
        return redirect('index:index')
    profile.delete()
    return redirect('index:index')
