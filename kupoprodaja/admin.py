from django.contrib import admin
from .models import User, Ugovor, Gorivo,PoslovnaJedinica, Preduzece, UserProfile, VrstaVozila, Broker, Banka, BankovniIzvod, StavkeBankovnogIzvoda

admin.site.register(User)
admin.site.register(Ugovor)
admin.site.register(Gorivo)
admin.site.register(PoslovnaJedinica)
admin.site.register(Preduzece)
admin.site.register(VrstaVozila)
admin.site.register(UserProfile)
admin.site.register(Broker)
admin.site.register(Banka)
admin.site.register(BankovniIzvod)
admin.site.register(StavkeBankovnogIzvoda)


