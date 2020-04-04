from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """ Customer Records """

    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length= 100, null=True)
    profile_pic = models.ImageField(default='amazon.png',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # print("hello",type(user))
    def __str__(self):
        return self.name or str(self.user)


class Tags(models.Model):
    """ Product Tags """
    name = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    """ Product Records """

    CATEGORY =(
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    tags = models.ManyToManyField(Tags)
    price = models.FloatField(null=True)
    name = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """ Order Records """

    STATUS = (
        ('Pending','Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True,  on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True,  on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    note = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.product.name








