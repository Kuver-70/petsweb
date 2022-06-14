from django.contrib import admin
from .models import Post, Pet, PetKind

admin.site.register(Post)
admin.site.register(Pet)
admin.site.register(PetKind)

admin.AdminSite.site_header = 'Pets Social Web Admin panel'
admin.AdminSite.site_title = 'Pets Social Web Admin panel'