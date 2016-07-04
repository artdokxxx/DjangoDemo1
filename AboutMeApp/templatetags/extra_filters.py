from django import template
from datetime import date

register = template.Library()


@register.filter
def get_age(value):
    date_diff = date.today()-value
    return (date_diff.days + date_diff.seconds / 86400) / 365.2425
