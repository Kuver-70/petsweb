from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


#class UserProfile(generic.DetailView):
#    form_class = UserChangeForm
#    template_name = 'profile.html'
#    success_url = reverse_lazy('pets_web:home')


def userprofile(request, pk):
    user_name = User.objects.get(pk=pk)
    context = {'user_name': user_name}
    return render(request, 'profile.html', context)
    #return HttpResponse("The page is under construction, dear %s." % user_name)


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('pets_web:home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    #success_url = reverse_lazy('pets_web:home')
    success_url = reverse_lazy('members:password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')