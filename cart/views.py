from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    # this view renders the cart contents
    return render(request, 'cart.html')

@login_required   
def add_to_cart(request, id):
    #view to add a quantity of specified Features to the cart
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
@login_required   
def adjust_cart(request, id):
    # This view is for ajusting  the quantity of Features
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))