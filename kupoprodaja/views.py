from django.db.models.query_utils import Q, select_related_descend
from django.forms.models import model_to_dict
from pkg_resources import Requirement
from Ugovori.settings import STATIC_ROOT
from django.db.models.query import QuerySet, prefetch_related_objects
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import HttpResponseRedirect
from django.db.models import Max, Sum, Count, Prefetch
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.views import generic
from .models import Preduzece, Ugovor, VrstaVozila, User, PoslovnaJedinica, Gorivo
from .forms import  UgovorModelForma, UserForm
from django.contrib.messages.views import SuccessMessageMixin
from .utils import render_to_pdf
from django.template.loader import get_template
from Ugovori.settings import STATICFILES_DIRS
import os
from pathlib import Path
import pathlib
from django.db.models import F, Func
from django.contrib.sessions.models import Session
from django.utils import formats
from datetime import datetime
from django.contrib import messages
class LandingPageView(LoginRequiredMixin, TemplateView):
    template_name= 'landing.html'

def landing_page(request):
    return render(request, 'landing.html')

class ListaUgovora(LoginRequiredMixin, generic.ListView):
    template_name='kupoprodaja/lista_ugovora.html'
    context_object_name='ugovori'

    def get_queryset(self):
        queryset= Ugovor.objects.all()
        user= self.request.user
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.filter(storno=False).order_by('-broj_ugovora')
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik).filter(storno=False).order_by('-broj_ugovora')
        else:
            queryset=queryset.filter(korisnik_id=self.request.user).filter(storno=False).order_by('-broj_ugovora')
        return queryset

class DetaljiUgovora(LoginRequiredMixin, generic.DetailView):
    template_name='kupoprodaja/detail_view.html'
    
    context_object_name='ugovor'
    
    def get_queryset(self):
        queryset= Ugovor.objects.all()
        user= self.request.user
        if user.is_superuser:
            queryset= Ugovor.objects.all()
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik)
        else:
            queryset=queryset.filter(korisnik_id=user)
        return queryset

class KreirajUgovor(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):

    model = Ugovor
    success_message = 'Ugovor je uspješno dodat!'
    error_message='Ugovor nije dodat! Pokušajte ponovo!'
    template_name='kupoprodaja/kreiraj_ugovor.html'
    fields=[
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
            'vrijednost_vozila',
            'datum',
            'napomena',
            'masa_vozila',
            'cijena',
            'gorivo'  
    ]
    

    def form_valid(self, form):
        firma=Preduzece.objects.get(id=1)
        form.instance.korisnik = self.request.user
        form.instance.business_unit = self.request.user.poslovna_jedinica
        form.instance.cijena_neto = form.instance.cijena/(1+float(firma.stopa_pdv))
        form.instance.cijena_neto =round(form.instance.cijena_neto,2)
        form.instance.pdv= form.instance.cijena_neto * float(firma.stopa_pdv)
        form.instance.pdv = round(form.instance.pdv, 2)
        if not Ugovor.objects.exists():
            form.instance.broj_ugovora = 1
        else:
            form.instance.broj_ugovora =Ugovor.objects.aggregate(Max('broj_ugovora')).get('broj_ugovora__max') + 1
        
        return super(KreirajUgovor, self).form_valid(form)
    
    def get_success_url(self):
        obj = self.object
        return reverse("kupoprodaja:detalji-ugovora", kwargs={'pk': self.object.pk})

class IzmjeniUgovor(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    template_name='kupoprodaja/izmjena_ugovora.html'
    success_message = 'Ugovor je uspješno dodat!'
    error_message='Ugovor nije dodat! Pokušajte ponovo!'
    model = Ugovor
    fields=[
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
            'vrijednost_vozila',
            'datum',
            'masa_vozila',
            'cijena',
            'ugovor_zakljucen',
            'gorivo',
            'napomena',
    ]
    success_message="Uspješno izmjenjeno!"
    def get_queryset(self):
        user= self.request.user
        queryset= Ugovor.objects.all()
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.all()
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik)
        else:
            queryset=queryset.filter(korisnik_id=self.request.user)
        return queryset
    def form_valid(self, form):
        firma=Preduzece.objects.get(id=1)
        form.instance.korisnik = self.request.user
        form.instance.business_unit = self.request.user.poslovna_jedinica
        form.instance.cijena_neto = form.instance.cijena/(1+float(firma.stopa_pdv))
        form.instance.cijena_neto =round(form.instance.cijena_neto,2)
        form.instance.pdv= form.instance.cijena_neto * float(firma.stopa_pdv)
        form.instance.pdv = round(form.instance.pdv, 2)
        
        return super(IzmjeniUgovor, self).form_valid(form)
    def get_success_url(self):
        return reverse("kupoprodaja:detalji-ugovora", kwargs={'pk': self.object.pk})

class BrisiUgovor(LoginRequiredMixin, generic.DeleteView):
    template_name='kupoprodaja/brisanje_ugovora.html'

    def get_queryset(self):
        queryset= Ugovor.objects.all()
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.all()
        else:
            queryset=queryset.filter(korisnik_id=self.request.user)
        return queryset
    def get_success_url(self):
        return reverse('kupoprodaja:lista-ugovora')

class KreirajKorisnika(LoginRequiredMixin, generic.CreateView):
    model=User
    template_name = 'kupoprodaja/create_user.html'
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
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return super(KreirajKorisnika, self).form_valid(form)
    def get_success_url(self):
        return reverse('kupoprodaja:lista-korisnika')

class ListaKorisnika(LoginRequiredMixin, generic.ListView):
    template_name='kupoprodaja/lista_korisnika.html'
    context_object_name='users'

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

class IzmjeniKorisnika(LoginRequiredMixin, generic.UpdateView):
    template_name='kupoprodaja/izmjena_korisnika.html'
    form_class = UserForm

    def get_queryset(self):
        queryset= User.objects.all()
        return queryset
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return super(IzmjeniKorisnika, self).form_valid(form)
    def get_success_url(self):
        return reverse("kupoprodaja:lista-korisnika")

class GeneratePDFContract(View):
    def get(self, request, *args, **kwargs):
        pk= kwargs.get('pk')
        ugovor = get_object_or_404(Ugovor, pk=pk)
        template = get_template('kupoprodaja/contract.html')
        preduzece = get_object_or_404(Preduzece)
        BASE_DIR = Path(__file__).resolve().parent.parent
        context = {
            'base_dir': BASE_DIR,
            'ugovor': ugovor,
            'firma': preduzece
        }
        html = template.render(context)
        pdf = render_to_pdf('kupoprodaja/contract.html', context)
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Ugovor_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class ContractStornoRequest(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    template_name='kupoprodaja/storno_request.html'
    model = Ugovor
    fields=[
            'broj_ugovora',
            'ime_komitent',
            'jib_komitent',
            'ime_kupac',
            'jib_kupac',
            'storno_request',
            'napomena'
    ]

    def get_queryset(self):
        user= self.request.user
        queryset= Ugovor.objects.all()
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.all()
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik)
        else:
            queryset=queryset.filter(korisnik_id=self.request.user)
        return queryset

    def get_initial(self):

        initial = super().get_initial()

        initial['storno_request'] = True

        return initial
    def get_success_url(self):
        return reverse("kupoprodaja:detalji-ugovora", kwargs={'pk': self.object.pk})

class ContractStatistics(LoginRequiredMixin, generic.ListView):
    template_name='kupoprodaja/storno_contract_status.html'
    def get_context_data(self, **kwargs):
        context = super(ContractStatistics, self).get_context_data(**kwargs)
        queryset= Ugovor.objects.all()
        user= self.request.user
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.all()
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik)
        else:
            queryset=queryset.filter(korisnik_id=self.request.user)
        context.update({
            "contract_count": queryset.filter(storno=False).count(),
            "contract_storno": queryset.filter(storno=True).count(),
            "storno_waiting": queryset.filter(storno=False).filter(storno_request=True).count()
        }) 
        return context
    
    def get_queryset(self):
        queryset= Ugovor.objects.all()
        user= self.request.user
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.all().order_by('-datum')
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik).order_by('-datum')
        else:
            queryset=queryset.filter(korisnik_id=self.request.user).order_by('-datum')
        return queryset

class ContractStornoRequested(LoginRequiredMixin, generic.ListView):
    template_name='kupoprodaja/storno_contract_requested.html' 
    context_object_name ="ugovori"
    def get_queryset(self):
        queryset= Ugovor.objects.all()
        user= self.request.user
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.filter(storno=False).filter(storno_request=True).order_by('-datum')
            
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik).filter(storno=False).filter(storno_request=True).order_by('-datum')
           
        else:
            queryset=queryset.filter(korisnik_id=self.request.user).filter(storno=False).filter(storno_request=True).order_by('-datum')
            
        return queryset

class ContractStornoApproved(LoginRequiredMixin, generic.ListView):
    template_name='kupoprodaja/storno_contract_approved.html' 
    context_object_name ="ugovori"
    def get_queryset(self):
        queryset= Ugovor.objects.all()
        user= self.request.user
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.filter(storno=True).order_by('-datum')
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik).filter(storno=True).order_by('-datum')
        else:
            queryset=queryset.filter(korisnik_id=self.request.user).filter(storno=True).order_by('-datum')
        
        return queryset

class ContractStornoApprove(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    template_name='kupoprodaja/storno_request_approve.html'
    model = Ugovor
    fields=[
            'broj_ugovora',
            'ime_komitent',
            'jib_komitent',
            'ime_kupac',
            'jib_kupac',
            'storno',
            'napomena'
    ]
    def get_queryset(self):
        user= self.request.user
        queryset= Ugovor.objects.all()
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.all()
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik)
        else:
            queryset=queryset.filter(korisnik_id=self.request.user)
        return queryset
    def get_initial(self):
        initial = super().get_initial()
        initial['storno'] = True
        return initial
    def get_success_url(self):
        
        return reverse("kupoprodaja:storno-odobren")
class ContractStornoDiscard(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    template_name='kupoprodaja/storno_request_discard.html'
    model = Ugovor
    fields=[
            'broj_ugovora',
            'ime_komitent',
            'jib_komitent',
            'ime_kupac',
            'jib_kupac',
            'napomena'
    ]
    def get_queryset(self):
        user= self.request.user
        queryset= Ugovor.objects.all()
        if self.request.user.is_superuser:
            queryset= Ugovor.objects.all()
        elif user.bussines_unit_head:
            korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
            queryset= Ugovor.objects.filter(korisnik_id__in=korisnik)
        else:
            queryset=queryset.filter(korisnik_id=self.request.user)
        return queryset
    def form_valid(self, form):
        
        form.instance.storno = False
        form.instance.storno_request = False
        
        return super(ContractStornoDiscard, self).form_valid(form)
    def get_success_url(self):
        return reverse("kupoprodaja:storno-zahtjevi")

class Round(Func):
      function = 'ROUND'
      arity = 2

def is_valid_param(param):
    return param !='' and param is not None
         
class GenerateInvoiceList(View):
    def get(self, request, *args, **kwargs):
        BASE_DIR = Path(__file__).resolve().parent.parent
        user= self.request.user
        korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica).values('poslovna_jedinica')
        ugovor=request.session['ugovor']
        startdate=request.session['startdate']
        enddate=request.session['enddate']
        totalcijena = 0.00
        totalpdv=0.00
        totalukupno=0.00
        if user.is_superuser:
            poslovnice= PoslovnaJedinica.objects.annotate(pdv=Sum('ugovor__pdv', filter=Q(ugovor__in=ugovor)),\
            cijena=Sum('ugovor__cijena', filter=Q(ugovor__in=ugovor)), broj=Count('ugovor__cijena', filter=Q(ugovor__in=ugovor)),\
            cijena_neto=Sum('ugovor__cijena_neto', filter=Q(ugovor__in=ugovor))).prefetch_related(Prefetch('ugovor_set',
            ugovor, to_attr='stavke'))
        else:
            poslovnice= PoslovnaJedinica.objects.filter(id__in=korisnik).annotate(pdv=Sum('ugovor__pdv', filter=Q(ugovor__in=ugovor)),\
            cijena=Sum('ugovor__cijena', filter=Q(ugovor__in=ugovor)), broj=Count('ugovor__cijena', filter=Q(ugovor__in=ugovor)),\
            cijena_neto=Sum('ugovor__cijena_neto', filter=Q(ugovor__in=ugovor))).prefetch_related(Prefetch('ugovor_set',
            ugovor, to_attr='stavke'))

        
        totalcijena = ugovor.aggregate(Sum('cijena_neto'))
        totalcijena = {k: round(v, 2) for k, v in totalcijena.items()}
       
        totalpdv = ugovor.aggregate(Sum('pdv'))
        totalpdv = {k: round(v, 2) for k, v in totalpdv.items()}
        totalukupno = ugovor.aggregate(Sum('cijena'))
        totalukupno = {k: round(v, 2) for k, v in totalukupno.items()}

        template = get_template('kupoprodaja/invoice_list1.html')
        preduzece = get_object_or_404(Preduzece)
        context = {
                'base_dir': BASE_DIR,
                'poslovnice': poslovnice,
                'start': startdate,
                'end': enddate,
                'firma': preduzece,             
                'totalukupno':totalukupno,
                'totalcijena': totalcijena,
                'totalpdv': totalpdv,
                'user': user
            }
        html = template.render(context)
        pdf = render_to_pdf('kupoprodaja/invoice_list1.html', context)
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "KIF_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
    
def ReportView(request):
    pregled=request.GET.get('Pregled')
    user=request.user
    ugovor= Ugovor.objects.filter(storno=False)
    if request.user.is_superuser:
        ugovor= ugovor
    else:
        korisnik=User.objects.filter(poslovna_jedinica=user.poslovna_jedinica)
        ugovor= ugovor.filter(korisnik_id__in=korisnik)
    startdate=request.GET.get('start_date')
    enddate=request.GET.get('end_date')
    if is_valid_param(startdate):
        ugovor=ugovor.filter(datum__gte=(startdate))
    if is_valid_param(enddate):
        ugovor=ugovor.filter(datum__lte=(enddate))
    request.session['ugovor']=ugovor
    request.session['startdate']=startdate
    request.session['enddate']=enddate
    if pregled == 'Pregled':
        return GenerateInvoiceList.as_view()(request)
    return render(request, 'kupoprodaja/reports1.html', {'ugovori': ugovor}) 