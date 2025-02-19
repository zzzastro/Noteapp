from django import template
from django.template.defaultfilters import timesince

register = template.Library()

@register.filter(name='smart_timesince')
def smart_timesince(value):
    """Returns a smarter version of timesince"""
    time_diff = timesince(value)
    if time_diff.startswith('0'):
        return 'today'
    return f"{time_diff} ago"

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter(name='add_class')
def add_class(field, css_class):
    """Adds a CSS class to a form field."""
    # Ensure we are working with a BoundField
    if hasattr(field, 'widget'):
        existing_classes = field.widget.attrs.get('class', '')
        new_classes = f"{existing_classes} {css_class}".strip()
        return field.as_widget(attrs={'class': new_classes})
    return field  # Return the field unchanged if it doesn't have a widget