from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class PetKind(models.Model):
    CAT = 'Котейка'
    DOG = 'Собакен'
    CAVY = 'Морская свинка'
    HAMSTER = 'Хомяк'
    FISH = 'Рыбка'
    PET_CHOICES = [
        (CAT, 'Котейка'),
        (DOG, 'Собакен'),
        (CAVY, 'Морская свинка'),
        (HAMSTER, 'Хомяк'),
        (FISH, 'Рыбка')
    ]
    pet_kind = models.CharField(max_length=30, choices=PET_CHOICES)

    def __str__(self):
        return self.pet_kind

    def __add__(self, other):
        return self.pet_kind + other


class Pet(models.Model):
    pet_kind = models.ForeignKey(PetKind, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.DateField()
    MALE = 'Муж'
    FEMALE = 'Жен'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    ]
    breed = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    avatara = models.ImageField(max_length=100, blank=True)
    master = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_kind + ' ' + self.name

    def get_absolute_url(self):
        return reverse('pets_web:home')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()


class Post(models.Model):
    author = models.ForeignKey(Pet, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #text = models.TextField()
    text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('pets_web:post_detail', kwargs={'pk': self.id})
