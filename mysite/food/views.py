from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
# view is nothing but what content your user is going to view 

def index(request):
	item_list = Item.objects.all()
	
	context = { 
	   'item_list':item_list,
	}
	return render(request,'food/index.html',context)

def item(reuest):
	return HttpResponse('<h1>This is an item view</h1>')

def detail(request, item_id): # created item id for details of perticular food item only
    item = Item.objects.get(pk=item_id) # only want to get the object whose primery key = item id
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)
