from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def signupUser(request):
    page = 'signup'
    if request.method == 'POST':
        print('yes')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # print(username,email)

            if password1 != password2:
                form.add_error('password2', 'Passwords do not match')
                print('not')
            else:
                form.save()
                print('yes')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home') 
    else:
        form = CustomUserCreationForm()
    context={'page':page,'form':form}
    return render(request, 'user/register.html', context)

def loginUser(request):
    page='login'
    if request.method == 'POST':
        email = request.POST['email']
        # print(email)
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  
    context={'page':page}
    return render(request, 'user/register.html',context)
