import numbers
from .models import Ugovor

from django.db.models import Max
from kupoprodaja.models import Ugovor
from .forms import UgovorModelForma
from django.views.generic.edit import FormMixin, ModelFormMixin
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from num2words import num2words
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def number_to_letters(number):
    try:
        number = int(number)
        return num2words(number, lang='sr').replace('-', '.').title()
    except ValueError:
        return "Nije validan broj."
    
