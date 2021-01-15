from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import GroceryList
from .forms import GroceryListForm

def index(request):
    grocery_list = GroceryList.objects.order_by('-id')

    context = {
        'grocery_list': grocery_list
    }
    return render(request, 'grocerylist/index.html', context)

def create(request):
    description = request.POST['description']
    grocery_item = GroceryList(description=description)
    grocery_item.save()

    return HttpResponseRedirect(reverse('grocerylist:index'))

def purchased(request, id):
    grocery_item = get_object_or_404(GroceryList, pk=id)
    grocery_item.purchased = True
    grocery_item.save()

    return HttpResponseRedirect(reverse('grocerylist:index'))

def deleted(request, id):
    grocery_item = get_object_or_404(GroceryList, pk=id)
    grocery_item.delete()
    grocery_item.save()

    return HttpResponseRedirect(reverse('grocerylist:index'))
