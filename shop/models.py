from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='catgory')

    def __str__(self):
         return self.title


class Contact( models.Model):
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     subject = models.CharField(max_length=50)
     meesage = models.TextField
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.name
     
     #pets Category

class PetCategory(models.Model):
     pet_type_choices =(
          ('US', 'American Region'),
          ('IN', 'Indian Region')
     )
     title = models.CharField(max_length=50)
     image = models.ImageField(upload_to='pets')
     description = models.TextField()
     price = models.DecimalField(max_digits=10 , decimal_places=2)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     pet_type = models.CharField(max_length=10, choices=pet_type_choices)
     available = models.BooleanField(default=True)
     best_seller = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     phone = models.CharField(max_length=15)
     pet = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
     date = models.DateField()
     time = models.TimeField()
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

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

class Home(models.Model):
          name = models.CharField(max_length=30)
          description = models.TextField()
          image = models.ImageField(upload_to='home')
          created_at = models.DateTimeField(auto_now_add=True)





          


def  __str__(self):
          return self.name

           

                
     