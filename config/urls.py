"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('contact', contact_view,name='contact'),
    path('login', login_view,name='login'),
    path('register', register_view,name='register'),
    path('logout', logout_view,name='logout'),
    path('profile', profile_view,name='profile'),
    path('profile/edit', edit_profile_view,name='edit_profile'),

    # add pet 
    path('add/pet', add_pet_view,name='add_pet'),
    path('remove/pet/<int:id>', remove_pet_view,name='remove_pet'), 
    path('edit/pet/<int:id>', edit_pet_view,name='edit_pet'),
    path('view/pet/<int:id>', view_pet,name='view_pet'),
    path('view/pets', view_pets,name='view_pets'),
    path('add/vet', add_vet_view,name='add_vet'),
    path('vet/login', vet_login_view,name='vet_login'),
    path('view/vets', view_vets, name='view_vets'),
    path('vet/home', vet_home_view, name='vet_home'),
    path('article', article_view,name='article'),
    
    path('appointment', appointment_view,name='appointment'),
    path('services', TemplateView.as_view(template_name='services.html'), name='services'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('Departments', TemplateView.as_view(template_name='Departments.html'), name='Departments'),
    path('home', home_view, name='home'),
    path('vet/profile/<int:id>', vet_profile_view, name='vet_profile'),
    path('accept/appointment/<int:id>', accept_appointment, name='accept_appointment'),
    path('reject/appointment/<int:id>', reject_appointment, name='reject_appointment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
