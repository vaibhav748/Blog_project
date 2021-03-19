from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm, ProfilePicForm


# Create your views here.

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    my_dict = {'form': form, 'registered': registered}
    return render(request, 'App_Login/signup.html', context=my_dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_Login/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:signin'))


@login_required()
def profile(request):
    form1 = ProfilePicForm()
    return render(request, 'App_Login/profile.html', context={'form1': form1})


@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileForm(instance=current_user)
    my_dict = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileForm(instance=current_user)
            my_dict.update({'success': 'Profile Updated Successfully.'})
    my_dict.update({'form': form})
    return render(request, 'App_Login/change_profile.html', context=my_dict)


@login_required
def pass_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    success = False
    if request.method == "POST":
        form = PasswordChangeForm(current_user, request.POST)
        if form.is_valid():
            form.save()
            success = True
            return redirect("App_Login:signin")
    return render(request, 'App_Login/change_pass.html', context={'form': form, 'success': success})


@login_required
def pic_add(request):
    form = ProfilePicForm()
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid:
            user_obj = form.save(commit=False)
            if user_obj.user == request.user:
                user_obj.save()
                return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/change_pic.html', context={'form': form})


@login_required
def pic_change(request):
    form = ProfilePicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/change_pic.html', context={'form': form})






