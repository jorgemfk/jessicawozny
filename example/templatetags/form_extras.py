# en templatetags/form_extras.py
from django import template
import json
register = template.Library()

@register.filter(name='as_widget')
def as_widget(field, attrs):
    #try:
     #   attrs = json.loads(attrs.replace("'", '"'))
    #except Exception:
    #    attrs = {}
    return field.as_widget(attrs=eval(attrs))
