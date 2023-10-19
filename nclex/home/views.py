from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contact
# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, 'home/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Login successful")
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print("Error")
            return redirect('/login')
            
    if request.method == 'GET':
        return render(request, 'home/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password')
        if password == password1:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('Doneeeeeeeeeeeeeeeeee')
            return redirect('/')
        else:
            return redirect('/signup')
    else:
        return render(request, 'home/signup.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        print("done")
    
    return render(request, 'home/contact.html')