from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages

def signupUser(request):
    referrer = request.META.get('HTTP_REFERER', None)
    print(referrer)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
         
            welcome_message = "Welcome {}".format(username)
            messages.success(request, welcome_message)
            
            if referrer:
                return redirect(referrer) 
            else:
                return redirect('home') 
    else:
        form = SignUpForm()
        print(form.errors)
    return render(request, 'base/signup.html', {'form': form})

def loginUser(request):
    page = 'login'
    referrer = request.META.get('HTTP_REFERER', None)
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.userprofile.userType in ['doctor', 'admin']:
                messages.success(request, f"Welcome {user.userprofile.userType.capitalize()} {user.username}")
                return redirect('dashboard')
            else:
                messages.success(request, f"Welcome {user.username}")
                

            login_page_url = request.build_absolute_uri('/user/login/') 
            if referrer and referrer != login_page_url:
                return redirect(referrer)  
            else:
                return redirect('home') 
        else:
           
            messages.error(request, form.errors)
    else:
        form = LoginForm()
    context = {'page': page}
    return render(request, 'user/register.html', context)



def signoutUser(request):
    logout(request)
    return redirect('home')
