

from django import template
from django.utils.formats import number_format




register = template.Library()
@register.filter(name='format_currency')
def format_currency(value):
    # Format the number as 0.000,00
    formatted_value = number_format(value, decimal_pos=2, force_grouping=True, use_l10n=True)
    # Replace the decimal separator and thousands separator to match the desired format
    formatted_value = formatted_value.replace('.', '|').replace(',', '.').replace('|', ',')

    return formatted_value