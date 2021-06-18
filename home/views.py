from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Members
from .forms import FoodDonationForm, MoneyDonateForm, ContactForm
from users.forms import SubscriptionForm

def homepage(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            instance = form.save()
        return redirect('homepage')
        

    else:
        return render(request, 'index.html', {'form': ContactForm})

def about(request):
    return render(request, "about.html")

@login_required
def donate(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('donate')
        
    else:
        if Members.objects.filter(user = request.user).exists():
            is_distributor = True
        else:
            is_distributor = False
        print(is_distributor)
        return render(request, "donate.html", {'is_distributor': is_distributor, 'suscribe_form': SubscriptionForm, 'foodForm': FoodDonationForm, 'moneyForm': MoneyDonateForm})

@login_required
def food(request):
    form = FoodDonationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.manager = request.user
        instance.save()
    messages.success(request,('Food Donation Successful, Wait till someone arrives to help!'))  
    return redirect('donate')  

@login_required
def money(request):
    form = MoneyDonateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.manager = request.user
        instance.save()
    return redirect('donate')      


@login_required
def unsuscribe(request):
    member = Members.objects.get(user = request.user)
    member.delete()
    return redirect('donate')