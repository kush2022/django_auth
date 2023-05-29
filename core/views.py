from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from . forms import NewUserForm

# Create your views here.
def register_request(request):
    """
    This allows the user to register a user into the database 
    """

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
    
    form = NewUserForm()
    context = {
        "form": form
    }
    return render(request, 'core/register.html', context)



def login_request(request):
    """
    This is the view that allows users to login to the system 
    """

    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # errors

    form = AuthenticationForm()

    context = {
        'form': form 
    }
    return render(request, 'core/login.html', context)


def logout_request(request):
    logout(request)
    return redirect('login-page')