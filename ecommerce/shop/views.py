from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

from django.http.response import JsonResponse
from .models import Category,Product,CartItem,Wishlist

# Create your views here.

def index(request):
    return render(request, 'index.html', {'name' : request.user.username })
    # return render(request,"index.html")


# SIGNUP 

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'signup.html')


# LOGIN

def user_login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username1, password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("signup")
    return render(request, 'login.html')


# LOGOUT

def user_logout(request):
    logout(request)
    return redirect("login")



# CATEGORIES

def categories(request):
    categories = Category.objects.all().order_by('-name')
    context = {'categories': categories}
    return render(request, 'category.html', context)



# PRODUCTS

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category' : category,
        'categories' : categories,
        'products' : products,
    }
    return render(request, 'products-list.html', context)



# PRODUCT DETAILS

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    wishlist = Wishlist.objects.filter(product=product)
    context = {'product': product, 'wishlist': wishlist}
    return render(request, 'product-detail.html', context)


# CART 

def add_to_cart(request,  id, slug):
    product = Product.objects.get(id=id, slug=slug)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


# UPDATECART USING AJAX

def updatecart(request):
    if request.method == 'POST':
       prod_id = int(request.POST.get('product_id')) 
       if(CartItem.objects.filter(product_id=prod_id)):
           prod_qty = int(request.POST.get('product_qty'))
           cart = CartItem.objects.get(product_id=prod_id)
           cart.quantity = prod_qty
           cart.save()
           return JsonResponse({'status':"Updated Successfully"})
    return redirect('cart')


# REMOVE FROM CART 

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


# CHECKOUT 

def checkout(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'total_price': total_price})


# WISHLIST 

def wishlist(request):
    wishlist = Wishlist.objects.all()
    context = {'wishlist':wishlist}
    return render(request, 'wishlist.html', context)

def addtowishlist(request):
    if request.method == 'POST':
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id) 
            if(product_check):
                if(Wishlist.objects.filter(product_id=prod_id)):
                    return JsonResponse({'status':"Product already in wishlist"})
                else:
                    Wishlist.objects.create(product_id=prod_id)
                    return JsonResponse({'status':"Product added to wishlist"})
            else:
                return JsonResponse({'status':"No such product found"})
    return redirect('cart')


def remove_from_wishlist(request, wishlist_id):
    item = Wishlist.objects.get(id=wishlist_id)
    item.delete()
    return redirect('wishlist')

