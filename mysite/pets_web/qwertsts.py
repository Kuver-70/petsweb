#from .models import Post, Pet
from django.contrib.auth.models import User
from django.conf import settings
from .models import PetKind

a = PetKind.objects.all()

print(a)