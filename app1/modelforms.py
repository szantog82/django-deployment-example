from django import forms

from app1.models import Clients


class NewClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

