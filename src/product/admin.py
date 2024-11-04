from django.contrib import admin

# Register your models here.
from .models import Product
from .models import ProductImage
from  .models import ProductInfo

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductInfo)
