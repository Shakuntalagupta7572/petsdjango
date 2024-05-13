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
from shop.views import contact_view, login_view, vet_login_view, register_view, appointment_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('contact', contact_view,name='contact'),
    path('login', login_view,name='login'),
    path('vet/login', vet_login_view,name='vet_login'),
    path('register', register_view,name='register'),
    path('appointment', appointment_view,name='appointment'),
    path('services', TemplateView.as_view(template_name='services.html'), name='services'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('Departments', TemplateView.as_view(template_name='Departments.html'), name='Departments'),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
