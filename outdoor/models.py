from django.db import models





class Category(models.Model):
    id_category = models.CharField(primary_key=True, max_length=30, auto_created=False)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    id_product = models.CharField(primary_key=True, max_length=40, auto_created=False)
    product = models.CharField(max_length=60)
    prw_product = models.ImageField(upload_to='static/product', default='static/product/default.webp')

    def __str__(self):
        return self.product


class Subproduct(models.Model):
    parent = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, default='-')
    subproduct = models.CharField(max_length=60)
    prw_subproduct = models.ImageField(upload_to='static/subproduct', default='static/subproduct/default.webp')
    text_subproduct =models.TextField(null=True)
    price = models.CharField(max_length=60, default='0')
    unit = models.CharField(max_length=60, default='-')

    def __str__(self):
        return self.subproduct


class Portfolio(models.Model):
    picture = models.ImageField(upload_to='static/portfolio', default='static/portfolio/default.webp')
    text = models.CharField(max_length=200)




class Call(models.Model):
    client = models.CharField(max_length=60, default='-')
    phone = models.CharField(max_length=10, default='-')
    date = models.DateTimeField()
