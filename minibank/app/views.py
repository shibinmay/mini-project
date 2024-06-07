from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import home

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            data = home.objects.get(username=username, password=password)
            request.session['id'] = data.id
            return redirect(index)
        except home.DoesNotExist:
            return HttpResponse("Invalid username or password")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        aadhar = int(request.POST['aadhar'])
        place = request.POST['Place']
        age = request.POST['Age']
        initial_amount = int(request.POST['amount'])
        if initial_amount >= 1000:
            data = home.objects.create(fullname=fullname, email=email, username=username, password=password,
                                       aadhar=aadhar, place=place, age=age, initialamount=initial_amount)
            return redirect(login)
        else:
            return HttpResponse("Initial amount should be at least 1000")
    else:
        return render(request, 'register.html')

def logout(request):
    request.session.flush()
    return redirect(login)

def deposit(request):
    if 'id' in request.session:
        id = request.session['id']
        if not id:
            return redirect(index)
        data = home.objects.get(id=id)
        if request.method == 'POST':
            deposit_amount = int(request.POST.get('amount'))
            if deposit_amount:
                data.initialamount += deposit_amount
                data.save()
                messages.success(request, 'Deposit successful!')
                return redirect(profile)
        else:
            return render(request, 'deposit.html', {'data': data})
    else:
        return redirect(login)

def withdraw(request):
    if 'id' in request.session:
        id = request.session['id']
        if not id:
            return redirect(index)
        data = home.objects.get(id=id)
        if request.method == 'POST':
            withdraw_amount = int(request.POST.get('amount'))
            if withdraw_amount >= 500 and data.initialamount - withdraw_amount >= 500:
                data.initialamount -= withdraw_amount
                data.save()
                messages.success(request, 'Withdrawal successful!')
                return redirect(profile)
            else:
                return HttpResponse('Error')
        else:
            return render(request, 'withdraw.html', {'data': data})
    else:
        return redirect(login)

def profile(request):
    if 'id' in request.session:
        id = request.session['id']
        data = home.objects.get(id=id) 
        return render(request, 'profile.html' , {'data': data})
    else:
        return redirect(login)
  