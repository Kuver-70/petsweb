from pets_web.models import Pet
from django.views.generic import CreateView
from pets_web.forms import PetForm


class PetAddView(CreateView):
    model = Pet
    template_name = 'pet_add.html'
    form_class = PetForm



# Create your views here.
