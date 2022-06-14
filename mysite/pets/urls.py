from django.urls import path
from .views import PetAddView


app_name = 'pets'
urlpatterns = [
    path('add/', PetAddView.as_view(), name='pet_add'),
    #path('profile/<int:pk>', userprofile, name='profile'),
]
