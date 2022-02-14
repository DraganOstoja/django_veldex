from django.contrib import admin
from .models import User, Ugovor, Gorivo,PoslovnaJedinica, Preduzece, UserProfile, VrstaVozila

admin.site.register(User)
admin.site.register(Ugovor)
admin.site.register(Gorivo)
admin.site.register(PoslovnaJedinica)
admin.site.register(Preduzece)
admin.site.register(VrstaVozila)
admin.site.register(UserProfile)
