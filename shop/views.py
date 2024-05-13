from django.shortcuts import render ,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('home')

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
                # should not be in group vet
                if user.groups.filter(name='vet').exists():
                    messages.error(request, "You are a vet, please login from vet login page")
                else:
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
                if user.groups.filter(name='vet').exists():
                    login(request, user)
                    messages.success(request, "You have been logged in successfully")
                    return redirect('vet_home')
                else:
                    messages.error(request, "You are not a vet")
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
        password2 = request.POST.get('cpassword')
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

def profile_view(request):
    if request.user.groups.filter(name='vet').exists():
        return redirect('vet_home')
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'profile.html', {
        'pets':pets
    })

def edit_profile_view(request):
    if request.user.groups.filter(name='vet').exists():
        return redirect('vet_home')
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {
        'form':form
    })


def add_pet_view(request):
    if request.user.groups.filter(name='vet').exists():
        return redirect('vet_home')
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            messages.success(request, "Pet added successfully")
            return redirect('profile')
    return render(request, 'add_pet.html', {
        'form':form
    })

def remove_pet_view(request, id):
    pet = Pet.objects.get(id=id)
    pet.delete()
    messages.success(request, "Pet removed successfully")
    return redirect('profile')

def edit_pet_view(request, id):
    pet = Pet.objects.get(id=id)
    form = PetForm(instance=pet)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save()
            messages.success(request, "Pet updated successfully")
            return redirect('profile')
    return render(request, 'edit_pet.html', {
        'form':form
    })

def view_pets(request):
    if request.user.groups.filter(name='vet').exists():
        return redirect('vet_home')
    pets = Pet.objects.all()
    return render(request, 'view_pets.html', {
        'pets':pets
    })

def view_pet(request, id):
    pet = Pet.objects.get(id=id)
    return render(request, 'view_pet.html', {
        'pet':pet
    })

def add_vet_view(request):
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to access this page")
        return redirect('home')    
    form = VetForm()
    if request.method == 'POST':
        form = VetForm(request.POST, request.FILES)
        if form.is_valid():
            vet = form.save(commit=False)
            # create a new user
            user = User.objects.create_user(username=vet.email, email=vet.email, password=request.POST.get('password'))
            user.save()
            vet.user = user
            group = Group.objects.get(name='vet')
            vet.save()
            group.user_set.add(user)
            messages.success(request, "Vet added successfully")
            return redirect('view_vets')
    return render(request, 'add_vet.html', {
        'form':form
    })

def appointment_view(request):
    pets = Pet.objects.filter(user=request.user)
    vets = VetProfile.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pet = request.POST.get('pet')
        vet = request.POST.get('vet')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        print(name, email, phone, pet, vet, date, time, message)
        if len(name) > 0 and len(email) > 0 and len(phone) > 0:
            pet = Pet.objects.get(id=pet)
            vet = VetProfile.objects.get(id=vet)
            vet_user = vet.user
            appointment = Appointment(name=name, email=email, phone=phone, pet=pet, vet=vet_user,  date=date, time=time, message=message)
            appointment.save()
            messages.success(request, "Appointment booked successfully")
            return redirect('home')
        else:
            messages.error(request, "Please fill in all the fields!")
       
    return render(request, 'appointment.html', {
        'pets':pets,
        'vets':vets
    })
 
    
def services_view(request):
    return render(request, 'services.html')

def about_view(request):
    return render(request, 'about.html')

def departments_view(request):
    return render(request, 'departments.html')

def home_view(request):
    return render(request, 'home.html')

def vet_profile_view(request, id):
    vet = VetProfile.objects.get(id=id)
    return render(request, 'j.html')

def view_vets(request):
    vets = VetProfile.objects.all()
    return render(request, 'view_vets.html', {
        'vets':vets
    })

def vet_home_view(request):
    if not request.user.groups.filter(name='vet').exists():
        messages.error(request, "You are not authorized to access this page")
        return redirect('home')
    
    vet = VetProfile.objects.get(user=request.user)
    appointments = Appointment.objects.filter(vet=request.user)
    return render(request, 'vet_home.html', {
        'appointments':appointments, 
        'vet':vet
    })

# accept appointment
def accept_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.appointment_status = 'A'
    appointment.save()
    messages.success(request, "Appointment accepted successfully")
    return redirect('vet_home')

# reject appointment
def reject_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.appointment_status = 'C'
    appointment.save()
    messages.success(request, "Appointment rejected successfully")
    return redirect('vet_home')

def article_view(request):
    return render(request, 'article.html')









