from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ChangePasswordForm, CustomAuthenticationForm
from django.contrib.auth.models import User


def custom_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def users_list(request):
    users = User.objects.filter(groups__name='Clients')
    return render(request, 'users/users_list.html', {'users': users})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/registration.html', {'form': form})


def change_password_view(request):
    """View to change the password of a logged-in user."""
    form = ChangePasswordForm(user=request.user, data=request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        new_password = form.cleaned_data['new_password1']
        new_password2 = form.cleaned_data['new_password2']
        if new_password == new_password2:
            request.user.set_password(new_password)
            request.user.save()
            return redirect("home")
        else:
            form.add_error('new_password2', 'Hesla se neshodují.')

    return render(request, 'salon_ingrid_api/change_password.html', {"form": form})

