from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import (
    UserRegistrationForm
)


def login_user(request):
    return render(request, 'login.html')


def register_user(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registration sucessful")
            return redirect('login')

    context = {
        "form": form
    }
    return render(request, 'registration.html', context)
