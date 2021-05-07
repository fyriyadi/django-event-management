from django.shortcuts import render, redirect
from .forms import RegisterUserForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def homePage(request):
	return render(request, 'home.html')


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
    	form = CreateUserForm(request.POST)
    	if form.is_valid():
    		form.save()
    		user = form.cleaned_data.get('username')
    		messages.success(request, 'Account was created for ' + user)

    		return redirect('login')		
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

