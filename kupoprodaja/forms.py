from django.forms import widgets
from django.forms.widgets import HiddenInput
from kupoprodaja.models import Ugovor

from django.db.models import Max
from django import forms
from django.utils import timezone
from .models import Ugovor, User	
from django.contrib.admin import widgets

class UgovorModelForma(forms.ModelForm):
    class Meta:
        model = Ugovor
        fields= (
            'broj_ugovora',
            'ime_komitent',
            'jib_komitent',
            'lk_komitent',
            'ulica_komitent',
            'grad_komitent',
            'ime_kupac',
            'jib_kupac',
            'lk_kupac',
            'ulica_kupac',
            'grad_kupac',
            'vrsta_vozila',
            'marka_vozila',
            'broj_sasije',
            'broj_motora',
            'godiste',
            'opis',
            'boja',
            'zapremina',
            'snaga',
            'nosivost',
            'sjedista',
            'reg_oznaka',
            'cijena',
            'datum',
            'vrijednost_vozila',
            'ugovor_zakljucen',
            'napomena',
            'korisnik',
            'masa_vozila',
            'gorivo'            
        )

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ["password",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "poslovna_jedinica",
        "bussines_unit_head"
        ]
class DateInput(forms.DateInput):
    input_type = 'date'
    

CHOICES=(
        ("link", "Kif po poslovnicama")
    )
