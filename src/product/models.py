from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to="ProductImages/")
    quantity = models.IntegerField()
    code = models.CharField(max_length=10)
    price = models.FloatField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, parent_link=True)
    image1 = models.ImageField(null=True, upload_to="ExtraProductImage/")
    image2 = models.ImageField(null=True, upload_to="ExtraProductImage/")
    image3 = models.ImageField(null=True, upload_to="ExtraProductImage/")

    def __str__(self):
        return str(self.product)


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, parent_link=True)
    network = models.TextField(max_length=2000, default='No Information at the moment')
    battery = models.TextField(max_length=2000, default='No Information at the moment')
    memory = models.TextField(max_length=2000, default='No Information at the moment')
    processor = models.TextField(max_length=2000, default='No Information at the moment')
    brand = models.TextField(max_length=2000, default='No Information at the moment')
