from django import template

register = template.Library()


@register.filter
def avatar_path(value):
    return '/my-gallery/' + value.name

@register.filter
def add_note_id(value, arg):
    return value + str(arg)
