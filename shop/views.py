from django.shortcuts import render ,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Appointment

def contact_view(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     email = request.POST.get('email')
     subject = request.POST.get('subject')
     message = request.POST.get('message')
     if len(name)> 0 and len(email)> 0 and len(subject)> 0 and len(message)> 0 :
        contact= Contact(name=name , email=email , subject=subject ,message=message)
        contact.save()
        messages.success(request,"Your message has been sent successfully")
        return redirect 
    else:
        messages.error(request, "Please fill in all the fields!")
    return render(request,'contact.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username) > 0 and len(password) > 0:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in successfully")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'login.html')

def vet_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username) > 0 and len(password) > 0:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in successfully")
                return redirect('vet_home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'vetlogin.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(username) > 0 and len(email) > 0 and len(password) > 0:
            if password != password2:
                messages.error(request, "Passwords do not match")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "You have been registered successfully")
                return redirect('login')
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'register.html')

def appointment_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pet = request.POST.get('pet')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        if len(name) > 0 and len(email) > 0 and len(phone) > 0 and len(pet) > 0 and len(date) > 0 and len(time) > 0 and len(message) > 0:
            appointment = Appointment(name=name, email=email, phone=phone, pet=pet, date=date, time=time, message=message)
            appointment.save()
            messages.success(request, "Your appointment has been booked successfully")
            return redirect('home')
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'appointment.html')
        

def services_view(request):
    return render(request, 'services.html')

def about_view(request):
    return render(request, 'about.html')

def departments_view(request):
    return render(request, 'departments.html')

def home_view(request):
    return render(request, 'home.html')




