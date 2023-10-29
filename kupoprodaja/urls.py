
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (ListaUgovora, 
                    BrisiUgovor, KreirajKorisnika, 
                    ListaKorisnika, IzmjeniKorisnika, GeneratePDFContract, ContractStatistics,
                    ContractStornoRequested, ContractStornoApproved, contract_storno_discard,
                    GenerateInvoiceList, ReportView, ContractDraft, contract_payment,export_excel, RekapitulacijaNova, kreiraj_ugovor, zakljuci_ugovor,
                    storno_request, contract_storno_approve, contract_payment_list, izmjeni_ugovor, search_view, bussines_unit_list, vehicle_type_list,
                    fuel_type_list,company_details, kreiraj_vrstu_vozila, izmjeni_vrstu_vozila, kreiraj_vrstu_goriva, izmjeni_vrstu_goriva, kreiraj_poslovnicu, izmjeni_poslovnicu,
                    view_request, view_occured, contract_view_approve, contract_view_discard, ListaZahtjevaPregled, kreiraj_banku, izmjeni_banku, banke_lista,
                    IzvodIzmjeniFunkcija, IzvodKreirajFunkcija, izvodi_lista, export_dnevnik_pojedinacno, export_dnevnik_zbirno, IzmjeniSifruKorisnika)


app_name = 'kupoprodaja'
urlpatterns = [
    path('', ListaUgovora.as_view(), name='lista-ugovora'),
    path('search/', login_required(search_view), name='search'),
    path('kreiraj/',login_required(kreiraj_ugovor) ,name = 'kreiraj-ugovor'),
    path('<int:pk>/izmjena/', login_required(izmjeni_ugovor), name='izmjena-ugovora'),
    path('<int:pk>/brisanje/', BrisiUgovor.as_view(), name='brisanje-ugovora'),
    path('kreirajkorisnika/', KreirajKorisnika.as_view(), name = 'kreiraj-korisnika'),
    path('listakorisnika', ListaKorisnika.as_view(), name='lista-korisnika'),
    path('<int:pk>/izmjene/', IzmjeniKorisnika.as_view(), name='izmjene-korisnika'),
    path('<int:pk>/izmjena/pdf/', GeneratePDFContract.as_view(), name='ugovor'),
    path('<int:pk>/storno/', login_required(storno_request), name='storno-request'),
    path('statistika/', ContractStatistics.as_view(), name='storno-statistika'),   
    path('stornozahtjevi/', ContractStornoRequested.as_view(), name="storno-zahtjevi"),
    path('stornoodobren/', ContractStornoApproved.as_view(), name="storno-odobren"),
    path('ugovornacrt/', ContractDraft.as_view(), name="ugovor-nacrt"),
    path('<int:pk>/potvrda/', login_required(contract_storno_approve), name="storno-potvrda"),
    path('<int:pk>/odbijanje/', login_required(contract_storno_discard), name="storno-odbij"),
    path('prometkif/', GenerateInvoiceList.as_view(), name='prometkif'),
    path('izvjestaji/', login_required(ReportView), name='izvjestaji'),
    path('<int:pk>/naplata/', login_required(contract_payment), name="naplata"),
    path('<int:pk>/naplaceno/', login_required(contract_payment_list), name="naplata-lista"),
    path('eksport/', login_required(export_excel), name='eksport'),
    path('rekapitulacija_nova/', RekapitulacijaNova,name='rekapitulacija-nova'),
    path('<int:pk>/izmjena/zakljuci/', login_required(zakljuci_ugovor), name='zakljucenje-ugovora'),
    path('poslovnice/', login_required(bussines_unit_list), name='lista-poslovnica'),
    path('vrstevozila/', login_required(vehicle_type_list), name='vrste-vozila'),
    path('vrstegoriva/', login_required(fuel_type_list), name='vrste-goriva'),
    path('firma/', login_required(company_details), name='podaci-firma'),
    path('kreirajvozilo/', login_required(kreiraj_vrstu_vozila), name='kreiraj-vrstu-vozila'),
    path('<int:pk>/izmjenivozilo/', login_required(izmjeni_vrstu_vozila), name='izmjena-vrste-vozila'),
    path('kreirajgorivo/', login_required(kreiraj_vrstu_goriva), name='kreiraj-vrstu-goriva'),
    path('<int:pk>/izmjenigorivo/', login_required(izmjeni_vrstu_goriva), name='izmjena-vrste-goriva'),
    path('kreirajposlovnicu/', login_required(kreiraj_poslovnicu), name='kreiraj-poslovnicu'),
    path('<int:pk>/izmjeniposlovnicu/', login_required(izmjeni_poslovnicu), name='izmjena-poslovnice'),
    path('<int:pk>/zahtjevpregled/', login_required(view_request), name="zahtjev-pregled"),
    path('<int:pk>/ugovorpregledan/', login_required(view_occured), name="ugovor-pregledan"),
    path('listapregled/', ListaZahtjevaPregled.as_view(), name="lista-pregled"),
    
    path('<int:pk>/potvrdapregleda/', login_required(contract_view_approve), name="pregled-potvrda"),
    path('<int:pk>/odbijanjepregleda/', login_required(contract_view_discard), name="pregled-odbij"),
    path('dodajbanku/', login_required(kreiraj_banku), name='kreiraj-banku'),
    path('<int:pk>/izmjenibanku/', login_required(izmjeni_banku), name='izmjena-banka'),
    path('banke/', login_required(banke_lista), name='banke-lista'),
    path('dodajizvod/',  IzvodKreirajFunkcija.as_view(), name='izvod-kreiraj'),
    path('<int:pk>/izmjenaizvoda/', IzvodIzmjeniFunkcija.as_view(), name='izvod-izmjena'),
    path('izvodi/', login_required(izvodi_lista), name='lista-izvoda'),
    path('izv/', login_required(export_dnevnik_pojedinacno), name='rekapitulacija-pojedinacno'),
    path('zbirno/', login_required(export_dnevnik_zbirno), name='rekapitulacija-zbirno'),
    path('<int:pk>/izmjenesifre/', IzmjeniSifruKorisnika.as_view(), name='izmjene-sifre'),
]
