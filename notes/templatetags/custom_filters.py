from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Adds a CSS class to a form field."""
    # Ensure we are working with a BoundField
    if hasattr(field, 'widget'):
        existing_classes = field.widget.attrs.get('class', '')
        new_classes = f"{existing_classes} {css_class}".strip()
        return field.as_widget(attrs={'class': new_classes})
    return field  # Return the field unchanged if it doesn't have a widget