from django.shortcuts import (
    render,
    redirect,
    get_list_or_404
)
from django.contrib.auth import (
    authenticate, 
    login,
    logout
)
from .forms import (
    CreateUserForm
)
from django.contrib import messages


def signUpView(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            return redirect('accounts:login')
            messages.success(
                request, 'Account created for ' + user + ' login details have been sent to ' + email)

    context = {
        'form': form
        }
    return render(request, 'accounts/signup.html', context)


def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:home')
    
        else:
            messages.info(
                request,
                'username and password are case sensitive and/or username and password did not match'
            )

        

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('accounts:login')