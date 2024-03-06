from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, default=1)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return '{}'.format(self.name)


# PRODUCT
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True, default=1)
    slug = models.SlugField()
    color = models.CharField(max_length=250, default="Black")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    brand = models.CharField(max_length=250, default="Babyhug")
    image = models.ImageField(upload_to='products', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)


# CART
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    

# WISHLIST 
class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

