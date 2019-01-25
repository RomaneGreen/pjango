from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from renmo.forms import RegistrationForm


def home(request):
	return render(request, 'home.html')




def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration/reg_form.html', args)