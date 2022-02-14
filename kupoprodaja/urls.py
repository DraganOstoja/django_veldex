
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (ListaUgovora,DetaljiUgovora, KreirajUgovor, 
                    IzmjeniUgovor, BrisiUgovor, KreirajKorisnika, 
                    ListaKorisnika, IzmjeniKorisnika, GeneratePDFContract, ContractStornoRequest,ContractStatistics,
                    ContractStornoRequested, ContractStornoApproved, ContractStornoApprove, ContractStornoDiscard,
                    GenerateInvoiceList, ReportView
)


app_name = 'kupoprodaja'
urlpatterns = [
    path('', ListaUgovora.as_view(), name='lista-ugovora'),
    path('kreiraj/', KreirajUgovor.as_view(),name = 'kreiraj-ugovor'),
    path('<int:pk>/', DetaljiUgovora.as_view(), name='detalji-ugovora'),
    path('<int:pk>/izmjena/', IzmjeniUgovor.as_view(), name='izmjena-ugovora'),
    path('<int:pk>/brisanje/', BrisiUgovor.as_view(), name='brisanje-ugovora'),
    path('kreirajkorisnika/', KreirajKorisnika.as_view(), name = 'kreiraj-korisnika'),
    path('listakorisnika', ListaKorisnika.as_view(), name='lista-korisnika'),
    path('<int:pk>/izmjene/', IzmjeniKorisnika.as_view(), name='izmjene-korisnika'),
    path('<int:pk>/pdf/', GeneratePDFContract.as_view(), name='ugovor'),
    path('<int:pk>/storno/', ContractStornoRequest.as_view(), name='storno-request'),
    path('statistika/', ContractStatistics.as_view(), name='storno-statistika'),
    path('stornozahtjevi/', ContractStornoRequested.as_view(), name="storno-zahtjevi"),
    path('stornoodobren/', ContractStornoApproved.as_view(), name="storno-odobren"),
    path('<int:pk>/potvrda/', ContractStornoApprove.as_view(), name="storno-potvrda"),
    path('<int:pk>/odbijanje/', ContractStornoDiscard.as_view(), name="storno-odbij"),
    path('prometkif/', GenerateInvoiceList.as_view(), name='prometkif'),
    path('izvjestaji/', login_required(ReportView), name='izvjestaji')
]
