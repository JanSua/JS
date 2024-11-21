from django import template

register = template.Library()

@register.filter
def add_class(value, class_name):
    """
    Añade la clase CSS al widget de un campo de formulario.
    """
    return value.as_widget(attrs={'class': class_name})
