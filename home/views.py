from django.shortcuts import render
from django.utils import timezone
from products.models import Category
def home(request):

    return render(request,'home/home.html',{'cats':Category.objects.filter(parent_id=0)})
