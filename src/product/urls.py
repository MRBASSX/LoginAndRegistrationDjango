from django.urls import path

from .views import ProductList, ProductDetail, productDetail2
from .views import Home

urlpatterns = [
    path("product-list/", ProductList.as_view(), name="product-cart"),
    path("product-detail/<int:product_id>", productDetail2, name="product"),
    path("product-detail/<int:pk>", ProductDetail.as_view(), name="product"),
    path("home/", Home, name="home"),

]
