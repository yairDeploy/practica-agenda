from django.forms import inlineformset_factory

from agenda.forms.telefonoForm import TelefonoForm
from agenda.models import Contacto, Telefono


TelefonoFormSet = inlineformset_factory(
    Contacto,
    Telefono,
    form=TelefonoForm,
    extra=1,
    can_delete=True
)