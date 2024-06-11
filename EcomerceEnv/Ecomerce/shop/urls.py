from .views import index,product_detail,add_to_cart
from django.urls import path

urlpatterns = [
    path("",index,name="product"),
    path("product/<int:id>",product_detail,name="product_detail"),
    path("add_to_cart/<int:id>",add_to_cart,name="add_to_cart")
]