from django import template
from ..import models

register=template.Library()

@register.simple_tag
def title_tag():
    return "سایت من"
@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return{
    "category":models.Category.objects.filter(status=True)
    }
