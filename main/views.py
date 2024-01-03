from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Product, Cart
from authentication.models import VogueUser
from django.contrib.auth.decorators import login_required


def store(request):
    products = Product.objects.all()
    if request.method=='POST':
        query = request.POST.get("query")
        results = Product.objects.filter(Q(keywords__icontains=query) | Q(title__icontains = query))
        return render(request, "store.html", {'products': results, 'Searched': query})  
      
    return render(request, "store.html", {'products': products, 'Searched': False})

@login_required(login_url='/Signup')
def cart(request):
    cart_instance = Cart.objects.filter(user=request.user)
    return render(request, "cart.html", {'cart': cart_instance[0].products.all()})

def add_to_cart(request,pd_id):
    cart = Cart.objects.get(user=request.user)
    products = Product.objects.get(id=pd_id)
    cart.products.add(products)
    return redirect('/store')
def deleteitem(request,pd_id):
    cart = Cart.objects.get(user=request.user)
    products = Product.objects.get(id=pd_id)
    cart.products.remove(products)
    return redirect('/cart')
def product(request, pd_id):
    products = Product.objects.get(id=pd_id)
    return render(request, "product.html", {'pd': products})

@login_required(login_url="/Signup")
def checkout(request, pd_id):
    products = Product.objects.get(id=pd_id)
    sizes=products.size.split(',')
    print(sizes)
    return render(request, "checkout.html", {'pd': products, 'sizes':sizes})