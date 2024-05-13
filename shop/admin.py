from django.contrib import admin
from .models import Category
from .models import Contact
from .models import PetCategory
from .models import Appointment
from .models import services
from .models import about
from .models import Departments
from .models import Home

# Register your models here.
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(PetCategory)
admin.site.register(Appointment)
admin.site.register(services)
admin.site.register(about)
admin.site.register(Departments)
admin.site.register(Home)