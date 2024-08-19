from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Item

from .forms import ItemForm


# Create your views here.
def home(request):
        return render(request, 'home.html')

def about(request):
        return render(request, 'about.html')

def contact(request):
        return render(request, 'contact.html')

def create(request):
    context = {}
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('list')
        else:
            context['form']= form
    return render(request, 'items/create.html', context)

def list(request):
    items = Item.objects.all()
    return render(request, 'items/list.html', {'items': items})