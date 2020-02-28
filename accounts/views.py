from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import sign_in_form, register_form


@login_required
def get_sign_out(request):
    # signs the user out 
    auth.logout(request)
    messages.success(request, "Logout successful!")
    return redirect(reverse('home'))


def get_sign_in(request):
    # signs the user in
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        form_sign_in = sign_in_form(request.POST) 
        if form_sign_in.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Login successful!")
                return redirect(reverse('home'))
            else:
                form_sign_in.add_error(None, "Your username or password is incorrect!")
    else:
        form_sign_in = sign_in_form()
    return render(request, "../templates/sign_in.html", {"form_sign_in": form_sign_in})


def get_register(request):
    # allows the user to create an account
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        form_register = register_form(request.POST)

        if form_register.is_valid():
            form_register.save()

            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "you have registered!")
                return redirect(reverse('home'))

            else:
                messages.error(request, "Unable to register account.")

    else:
        form_register = register_form()
    return render(request, "../templates/register.html", {"form_register": form_register})
