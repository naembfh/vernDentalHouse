from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

def signupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = SignUpForm()
    return render(request, 'base/signup.html', {'form': form})

def loginUser(request):
    page='login'
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = LoginForm()
    context={'page':page}
    return render(request, 'user/register.html', context)



def signoutUser(request):
    logout(request)
    return redirect('home')
