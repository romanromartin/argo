
from outdoor.models import  Category, Subproduct
from django import template



register = template.Library()


@register.filter
def index(indexable, i):
    indexable.objects.filter(parent=i)
    return indexable
