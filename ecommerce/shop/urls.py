from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),

    path('signup/', signup, name="signup"),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),

    path('products/', product_list, name="product_list"),
    path('products/<slug:category_slug>', product_list, name="products_list_by_category"),
    path('categories/', categories, name="category"),
    path('product/<int:id>/<slug:slug>/',product_detail, name='product_detail'),

    path('add-to-cart/<int:id>/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/',cart, name='cart'),

    path('updatecart', updatecart, name='updatecart'),

    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),

    path('checkout/', checkout, name='checkout'),

    path('wishlist/', wishlist, name='wishlist'),
    path('add-to-wishlist', addtowishlist, name='addtowishlist'),
    path('remove-from-wishlist/<int:wishlist_id>/', remove_from_wishlist, name='remove_from_wishlist'),

]


