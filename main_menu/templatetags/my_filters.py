from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def is_on_the_page(url):
    return reverse(url)

@register.filter
def stringify(value):
    return mark_safe(value)