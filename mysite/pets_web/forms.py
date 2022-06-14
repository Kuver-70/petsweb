from django import forms
from .models import Post, Pet
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        users_id = User.pk
        pets_list = Pet.objects.filter(master=1)  # Надо вернуть список животных определенного юзера users_id
        model = Post
        fields = ('author', 'title', 'text')
        choices = [1, 2]
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}, choices=[1, 2, 3]),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pet', 'id': 'user'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'choices': [1, 2, 3, 4, 5]}),
            #'author': forms.ChoiceField(widget=forms.Select, choices=[1, 2, 3]),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('pet_kind', 'name', 'age', 'breed', 'description', 'master')

        widgets = {
            'pet_kind': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            #'age': forms.DateField(), #attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            #'master': forms.Select() # сюда нужно добавить список юзеров/питомцев ???
            'master': forms.TextInput(attrs={'class': 'form-control'}),
            #'avatara': forms.ImageField(),  # (attrs={'class': 'form-control'}),
        }


    '''    widgets = {
            'pet_kind': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.DateField(), #(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'avatara': forms.ImageField(), #(attrs={'class': 'form-control'}),
        }
'''