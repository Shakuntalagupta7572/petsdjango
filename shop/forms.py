from django import forms
from .models import *

# user profile form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        exclude = ['user']

class VetForm(forms.ModelForm):
    class Meta:
        model = VetProfile
        fields = '__all__'
        exclude = ['user']
