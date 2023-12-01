from django import forms 
from .models import *

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'title', 'description']


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'title', 'description']

class AssignTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['engineer']