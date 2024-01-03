from django.db import models
from authentication.models import VogueUser
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    description = models.TextField(verbose_name="Short Description (max: 30 words)")
    long_description = models.TextField(verbose_name="Detailed Description (max: 80 words)")
    size = models.TextField(verbose_name="Sizes (seperated by comma (,):")
    image = models.ImageField(upload_to='images/')
    auximage1 = models.ImageField(verbose_name="Extra Image1 (optional)",upload_to='images/', blank=True, null=True)
    auximage2 = models.ImageField(verbose_name="Extra Image2 (optional)",upload_to='images/', blank=True)
    auximage3 = models.ImageField(verbose_name="Extra Image3 (optional)",upload_to='images/', blank=True, null=True)
    keywords = models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return str(self.user.username) + "'s Cart"