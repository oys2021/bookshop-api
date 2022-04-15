from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    Isbn=models.CharField(max_length=13)
    pages=models.IntegerField()
    price=models.IntegerField()
    description=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)

   

    def __str__(self):
        return self.title

class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['cart_id', '-created_at']
        

    def __str__(self):
        return f'{self.cart_id}'
