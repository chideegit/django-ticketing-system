from django import forms 
from .models import *

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class AssignTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['engineer']