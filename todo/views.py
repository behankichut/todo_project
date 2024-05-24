from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def add_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            item = Item.objects.create(name=name)
            html = render_to_string('partial.html', {'item': item})
            return HttpResponse(html)
    return HttpResponse(status=400)
