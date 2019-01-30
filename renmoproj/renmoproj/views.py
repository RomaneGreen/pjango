import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from renmo.models import UserProfile,TokenTransfer
from django.db.models import F
from renmo.forms import TokenTransferForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from renmo.forms import RegistrationForm,EditProfileForm
from django.contrib import messages 
from django.conf import settings 
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
 transactions = TokenTransfer.objects.all().order_by('-id')[:6]
 args = {'transactions': transactions}
 return render(request, 'home.html',args)


def add_token(request):
 transactions = TokenTransfer.objects.all()
 args = {'transactions': transactions}
 return render(request, 'add_token.html',args)


def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): 
    if request.method == 'POST':
       
        # userTokens = UserProfile.objects.all()[0]
        userTokens = UserProfile.objects.get(user=request.user)
        userTokens.tokens = F('tokens')+ 5
        userTokens.save()
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration/reg_form.html', args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'registration/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)


def transfer_token(request):
    uzer = UserProfile.objects.get(user=request.user)
    uza =  TokenTransfer.objects.last().reciever
    users = UserProfile.objects.all()
    if request.method == "POST":
        form = TokenTransferForm(request.POST)
    
        if form.is_valid():
            transfer = form.save(commit=False)
            transfer.sender = uzer
            uzer.tokens = F('tokens')- transfer.tokens
            uzer.save()
            transfer.transfer_time = timezone.now()
            transfer.reciever.tokens += 99
            transfer.save()

            uza.tokens = F('tokens')+ transfer.tokens
            uza.save()
            return redirect('/', pk=transfer.pk)
    else:
          form = TokenTransferForm()
    return render(request, 'send_token.html',{"form":form,"users":users})
    # return render(request,'send_token.html',{"error":error,"users":users,"form":form})