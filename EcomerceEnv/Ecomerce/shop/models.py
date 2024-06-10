from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    Category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    image=models.ImageField(upload_to="",null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product,through="CartItem")
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.quantity
    
    
    
    

    