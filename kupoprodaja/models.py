from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db.models import Max

class Ugovor(models.Model):
    broj_ugovora = models.IntegerField(verbose_name='Broj ugovora:')
    ime_komitent = models.CharField(max_length=150, verbose_name='Ime komitenta:')
    jib_komitent = models.CharField(max_length=13, verbose_name='JMBG/JIB komitenta:',validators= [RegexValidator(regex= '^.{13}$',message='Duzina mora biti 13 karaktera', code='nomatch')])
    lk_komitent = models.CharField(max_length=20, verbose_name='Lična karta komitenta:')
    ulica_komitent = models.CharField(max_length=100, verbose_name='Adresa komitenta:')
    grad_komitent = models.CharField( max_length=100, verbose_name='Grad:')
    ime_kupac = models.CharField( max_length=150, verbose_name='Ime kupca:')
    jib_kupac = models.CharField(max_length=13, verbose_name='JMBG/JIB kupca:',validators= [RegexValidator(regex= '^.{13}$',message='Duzina mora biti 13 karaktera', code='nomatch')])
    lk_kupac = models.CharField(max_length=50, verbose_name='Lična karta kupca:')
    ulica_kupac = models.CharField(max_length=100, verbose_name='Adresa kupca:')
    grad_kupac = models.CharField(max_length=100, verbose_name='Grad:')
    vrsta_vozila = models.ForeignKey("VrstaVozila",  on_delete=models.CASCADE, verbose_name='Vrsta vozila:')
    marka_vozila = models.CharField(max_length=100, verbose_name='Marka vozila:')
    broj_sasije = models.CharField(max_length=50, verbose_name='Broj šasije:')
    broj_motora = models.CharField(max_length=50, verbose_name='Broj motora:')
    godiste = models.IntegerField(verbose_name='Godište vozila:')
    opis = models.CharField( max_length=50, verbose_name='Model vozila:')
    boja = models.CharField(max_length=50, verbose_name='Boja vozila:')
    zapremina = models.IntegerField(verbose_name='Zapremina motora:')
    snaga = models.CharField(max_length=10, verbose_name='Snaga motora:')
    nosivost = models.CharField(max_length=10, verbose_name='Nosivost vozila:')
    sjedista = models.CharField(max_length=5, verbose_name='Broj sjedišta:')
    reg_oznaka = models.CharField(max_length=20, verbose_name='Registarska oznaka:')
    datum = models.DateField(default=timezone.now, verbose_name='Datum ugovora:')
    vrijednost_vozila = models.FloatField(max_length=10, verbose_name='Vrijednost vozila:')
    ugovor_zakljucen = models.BooleanField(default=False, verbose_name='Ugovor zaključen:')
    napomena = models.CharField(max_length=150, verbose_name='Napomena:')
    korisnik = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name='Korisnik')
    masa_vozila = models.CharField(max_length=20, verbose_name='Masa vozila:')
    gorivo = models.ForeignKey("Gorivo", on_delete=models.CASCADE, verbose_name='Vrsta goriva')
    cijena = models.FloatField(max_length=10,default=10.00, verbose_name='Cijena ugovora:')
    pdv = models.FloatField(max_length=10,default=0.00, verbose_name='PDV:')
    cijena_neto = models.FloatField(max_length=10,default=0.00, verbose_name='Cijena bez pdv:')
    storno_request = models.BooleanField(default=False, verbose_name='Potvrditi storno:')
    storno = models.BooleanField(default=False, verbose_name='Stornirano:')
    storno_date= models.DateField(default=timezone.now,null=True, blank=True, verbose_name='Datum storna:')
    business_unit=models.ForeignKey('PoslovnaJedinica', on_delete=models.CASCADE, verbose_name='Poslovna jedinica')


    def __str__(self):
        return f'{self.ime_kupac}'
    
class User(AbstractUser):
    pass
    poslovna_jedinica=models.ForeignKey("PoslovnaJedinica", on_delete=models.CASCADE, null=True)
    bussines_unit_head=models.BooleanField("Rukovodilac poslovnice", default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Gorivo(models.Model):
    tip_goriva = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.tip_goriva}'

class PoslovnaJedinica(models.Model):
    naziv= models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.naziv}'

class Preduzece(models.Model):
    naziv= models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)
    mjesto = models.CharField(max_length=100)
    postanski_broj = models.CharField(max_length=5)
    jib = models.CharField(max_length=13, validators= [RegexValidator(regex= '^.{13}$',message='Duzina mora biti 13 karaktera', code='nomatch')])
    pib = models.CharField(max_length=12, validators= [RegexValidator(regex= '^.{12}$',message='Duzina mora biti 12 karaktera', code='nomatch')])
    telefon = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    zracun = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    stopa_pdv= models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return f'{self.naziv}' 

class VrstaVozila(models.Model):
    vrsta_vozila = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.vrsta_vozila}'

def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)        
post_save.connect(post_user_created_signal, sender=User)