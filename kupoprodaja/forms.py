from django.forms import widgets
from django.forms.widgets import HiddenInput
from kupoprodaja.models import Ugovor, Preduzece, VrstaVozila, Gorivo, PoslovnaJedinica, Banka, BankovniIzvod, StavkeBankovnogIzvoda
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AutocompleteSelect
from .models import Ugovor, User	
from django.contrib.admin import widgets
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.helper import FormHelper
class UgovorModelForma(forms.ModelForm):
    class Meta:
        model = Ugovor
        fields= (
            
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
            #'boja',
            'zapremina',
            'snaga',
            'nosivost',
            #'sjedista',
            'reg_oznaka',
            #'cijena',
            'datum',
            'vrijednost_vozila',
            'napomena',
            #'korisnik',
            'masa_vozila',
            'gorivo',
            #'broker',
            'mjesto_zakljucenja',
            'datum_preuzimanja',
            'vrijeme_preuzimanja',
            'broj_punomoci',
            'broj_fiskalnog_racuna',
            'jmb_punomocnik',
            'lk_punomocnik',
            'telefon_komitent',
            'telefon_kupac',
            'ima_punomoc'
            
            
        )

class UgovorModelFormaIzmjene(forms.ModelForm):
    class Meta:
        model = Ugovor
        fields= (
            
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
            #'boja',
            'zapremina',
            'snaga',
            'nosivost',
            #'sjedista',
            'reg_oznaka',
            #'cijena',
            
            'datum',
            'vrijednost_vozila',
            'napomena',
            #'korisnik',
            'masa_vozila',
            'gorivo',
            #'broker',
            'mjesto_zakljucenja',
            'datum_preuzimanja',
            'vrijeme_preuzimanja',
            'broj_punomoci',
            'broj_fiskalnog_racuna',
            'broj_ugovora',
            'jmb_punomocnik',
            'lk_punomocnik',
            'telefon_komitent',
            'telefon_kupac',
            'ima_punomoc'
            
        )
class CompanyForm(forms.ModelForm):
    class Meta:
        model=Preduzece
        fields=("naziv",  
                 "adresa",     
                 "mjesto" ,   
                 "postanski_broj",
                 "jib",   
                 "pib" ,
                 "telefon",
                 "fax",
                 "zracun",
                 "mail",
                 "stopa_pdv",
                 "broj_rjesenja",
                 "porezni_broj",
                 "web_site")
class UgovorConfirmPaymentListForm(forms.ModelForm):
    class Meta:
        model = Ugovor
        fields= (
            'id',
            'broj_ugovora'
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
        "bussines_unit_head",
        "has_contracts",
        "has_invoices",
        "jmb_korisnika",
        "broj_telefona",
        "mjesto" ,
        "adresa" ,
        "licna_karta",
        ]
        
        labels= {
            "password": "lozinka",
            "is_superuser": "Status administratora",
            "username" : "Korisničko ime",
            "first_name": "Ime",
            "last_name" : "Prezime",
            "email": "mejl",
            "is_staff": "Status člana posade",
            "is_active": "Aktivan",
            "date_joined": "Datum pridruživanja",
            "poslovna_jedinica" : "Poslovna jedinica",
            "bussines_unit_head": "Šef poslovne jedinice",
            "has_contracts" : "Vidi ugovore",
            "has_invoices": "Vidi fakture",
            "jmb_korisnika": "JMB korisnika",
            "broj_telefona": "Broj telefona",
            "mjesto": "Mjesto",
            "adresa": "Adresa",
            "licna_karta": "Lična karta"
        }
        
        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['is_superuser'].widget.attrs['placeholder'] = 'Ukazuje da korisnik ima sve dozvole bez dodjeljivanja pojedinačnih dozvola.'
            self.fields['username'].widget.attrs['placeholder'] = 'Obavezan podatak. 150 karaktera ili manje. Dozvoljena su samo slova, cifre i karakteri @/./+/-/_ .'
            self.fields['is_staff'].widget.attrs['placeholder'] = 'Ukazuje da korisnik može da se prijavi na ovaj sajt za administraciju.'
            self.fields['is_active'].widget.attrs['placeholder'] = 'Označava da li se korisnik smatra aktivnim. Deselektujte ovo umjesto da brišete nalog.'

    
class UserFormUpdate(forms.ModelForm):
    class Meta:
        model= User
        fields= [
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "poslovna_jedinica",
        "bussines_unit_head",
        "has_contracts",
        "has_invoices",
        "jmb_korisnika",
        "broj_telefona",
        "mjesto" ,
        "adresa" ,
        "licna_karta",
        ]
        
        labels= {
            
            "is_superuser": "Status administratora",
            "username" : "Korisničko ime",
            "first_name": "Ime",
            "last_name" : "Prezime",
            "email": "mejl",
            "is_staff": "Status člana posade",
            "is_active": "Aktivan",
            "date_joined": "Datum pridruživanja",
            "poslovna_jedinica" : "Poslovna jedinica",
            "bussines_unit_head": "Šef poslovne jedinice",
            "has_contracts" : "Vidi ugovore",
            "has_invoices": "Vidi fakture",
            "jmb_korisnika": "JMB korisnika",
            "broj_telefona": "Broj telefona",
            "mjesto": "Mjesto",
            "adresa": "Adresa",
            "licna_karta": "Lična karta"
        }
        
        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['is_superuser'].widget.attrs['placeholder'] = 'Ukazuje da korisnik ima sve dozvole bez dodjeljivanja pojedinačnih dozvola.'
            self.fields['username'].widget.attrs['placeholder'] = 'Obavezan podatak. 150 karaktera ili manje. Dozvoljena su samo slova, cifre i karakteri @/./+/-/_ .'
            self.fields['is_staff'].widget.attrs['placeholder'] = 'Ukazuje da korisnik može da se prijavi na ovaj sajt za administraciju.'
            self.fields['is_active'].widget.attrs['placeholder'] = 'Označava da li se korisnik smatra aktivnim. Deselektujte ovo umjesto da brišete nalog.'
class UserPasswordUpdate(forms.ModelForm):
    class Meta:
        model= User
        fields= [
        "password",
        ]



class DateInput(forms.DateInput):
    input_type = 'date'

CHOICES=(
        ("link", "Kif po poslovnicama")
    )

class VrstaVozilaForm(forms.ModelForm):
    class Meta:
        model= VrstaVozila
        fields= [
            "vrsta_vozila"
        ]
        
        
class VrstaGorivaForm(forms.ModelForm):
    class Meta:
        model= Gorivo
        fields= [
            "tip_goriva"
        ]
        
class PoslovnaJedinicaForm(forms.ModelForm):
    class Meta:
        model= PoslovnaJedinica
        fields= [
            "naziv"
        ]
        
class BankaForm(forms.ModelForm):
    class Meta:
        model= Banka
        fields= [
            "naziv_banke",
            "sjediste_banke",
            "adresa_banke"
        ]
        
        
class IzvodKreiraj(forms.ModelForm):
    
    class Meta:
        model= BankovniIzvod
        fields=[
            'broj_izvoda',
            'banka',
            'datum_izvoda',
            'napomena',
            'zakljucen_izvod'
        ]
        widgets={
            'banka': forms.Select(attrs={
                'class': 'form-control',
                'id': 'banka_id'
            }),

        }
class IzvodIzmjena(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(IzvodIzmjena, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['bankovniizvod_id'].required = False
            

    class Meta:
        model = BankovniIzvod
        fields = [
            'broj_izvoda',
            'banka',
            'datum_izvoda',
            'napomena',
            'zakljucen_izvod',
            
        ]
        widgets = {
            'banka': forms.Select(attrs={
                'class': 'form-control',
                'id': 'banka_id'
            }),

        }

IzvodSubformSet = inlineformset_factory(
    BankovniIzvod,
    StavkeBankovnogIzvoda,formset=BaseInlineFormSet, 
    fields=('korisnik_uplatio',
            'opis',
            'uplata',
            'isplata',
            ),
    
    widgets={
            'korisnik_uplatio': forms.Select(attrs={
                
            }),
            
            },
    extra=0,
    labels={'korisnik_uplatio': "",
            'opis': "",
            'uplata': "",
            'isplata': "",
            'DELETE':  "",
            },
    
    can_order=True
)

IzvodSubformSetCreate = inlineformset_factory(
    BankovniIzvod,
    StavkeBankovnogIzvoda,formset=BaseInlineFormSet,
    fields=('korisnik_uplatio',
            'opis',
            'uplata',
            'isplata',
            ),
    
    widgets={
            'korisnik_uplatio': forms.Select(attrs={
                
            }),
            
            },
    extra=2,
    labels={'korisnik_uplatio': "",
            'opis': "",
            'uplata': "",
            'isplata': "",
            'DELETE':  "",
            },
    
    can_order=True
)


