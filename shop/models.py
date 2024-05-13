from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='catgory')

    def __str__(self):
         return self.title

class Profile(models.Model):
     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
     image = models.ImageField(upload_to='profile')
     phone = models.CharField(max_length=15)
     address = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.user.username

class Contact( models.Model):
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     subject = models.CharField(max_length=50)
     meesage = models.TextField
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.name
     
     #pets Category

class Pet(models.Model):
     pet_type_choices =(
          ('US', 'American Region'),
          ('IN', 'Indian Region'),
          ('CN', 'Chinese Region'),
     )
     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     title = models.CharField(max_length=50)
     image = models.ImageField(upload_to='pets')
     description = models.TextField()
     age = models.IntegerField(default=1)
     breed = models.CharField(max_length=50)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     pet_type = models.CharField(max_length=10, choices=pet_type_choices)
     has_vaccinated = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title

class Appointment(models.Model):
     appointment_status = (
          ('P', 'Pending'),
          ('A', 'Approved'),
          ('C', 'Cancelled'),
     )
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     phone = models.CharField(max_length=15)
     pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
     vet = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     date = models.DateField()
     time = models.TimeField()
     message = models.TextField(default='I want to make an appointment')
     created_at = models.DateTimeField(auto_now_add=True)
     appointment_status = models.CharField(max_length=1, choices=appointment_status, default='P')

class services(models.Model):
     name = models.CharField(max_length=30)
     description = models.TextField()
     image = models.ImageField(upload_to='services')
     price = models.DecimalField(max_digits=10, decimal_places=2)
     created_at = models.DateTimeField(auto_now_add=True)

class about(models.Model):
      
     name = models.CharField(max_length=30)
     description = models.TextField()
     image = models.ImageField(upload_to='about')
     created_at = models.DateTimeField(auto_now_add=True)

class Departments(models.Model):
     name = models.CharField(max_length=30)
     description = models.TextField()
     image = models.ImageField(upload_to='departments')
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.name

class Home(models.Model):
     name = models.CharField(max_length=30)
     description = models.TextField()
     image = models.ImageField(upload_to='home')
     created_at = models.DateTimeField(auto_now_add=True)

class VetProfile(models.Model):
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     phone = models.CharField(max_length=15)
     password = models.CharField(max_length=30)
     department = models.ForeignKey(Departments, on_delete=models.CASCADE)
     experience = models.IntegerField(default=1)
     fee = models.DecimalField(max_digits=10, decimal_places=2)
     image = models.ImageField(upload_to='vetprofile')
     created_at = models.DateTimeField(auto_now_add=True)
     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
       

          



           

                
     