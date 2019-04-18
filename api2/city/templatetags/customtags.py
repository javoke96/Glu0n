from django import template
from ..models import Cities

register = template.Library()

@register.simple_tag
def deleteall():
  	return Cities.objects.all().delete()
