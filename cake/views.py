from django.shortcuts import render
from .models import DataDiscription
# Create your views here.
def index(request):
    objs = DataDiscription.objects.all()
    #objs = DataDiscription.objects.filter(first_name='first_name')
    return render(request, 'index.html', {'cakes': objs})

def index2(request):
    o1 = DataDiscription()
    o1.name = 'Sponge Cake'
    o1.desc = "This is Sponge Cake"
    o1.price = 50
    o1.img = 'cake-1.jpg'

    o2 = DataDiscription()
    o2.name = 'Cheese Cake'
    o2.desc = "This is Cheese Cake"
    o2.price = 60
    o2.img = 'cake-2.jpg'

    o3 = DataDiscription()
    o3.name = 'Cheese Cake'
    o3.desc = "This is Cheese Cake"
    o3.price = 70
    o3.img = 'cake-3.jpg'

    objs = [o1, o2, o3]
    return render(request, 'index.html', {'cakes': objs})
