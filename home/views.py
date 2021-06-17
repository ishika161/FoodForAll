from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Members

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

@login_required
def donate(request):
    return render(request, "donate.html")

@login_required
def food(request):
    return render(request, "food.html")

@login_required
def money(request):
    return render(request, "money.html")

@login_required
def distributor(request):
    member = Members(user = request.user, distributor=True)
    member.save()
    return redirect('donate')
