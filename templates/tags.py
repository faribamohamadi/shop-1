from django import template
from django.utils import timezone
from products.models import Category
register = template.Library()
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import _html_escapes
@register.simple_tag
def assets():
    if timezone.localtime().hour >= 18 or timezone.localtime().hour < 6:
        return 'assets-dark'
    else:
        return 'assets-light'


@register.simple_tag
def GlobalName(lang='fa'):
    if lang == 'fa':
        return 'ویرا'
    if lang == 'en':
        return 'Vira'
@register.simple_tag
def base_header(request=None):
    sub_categories=Category.objects.filter(parent_id=0)
    return render_to_string('sub/header.html',{'sub_categories':sub_categories})