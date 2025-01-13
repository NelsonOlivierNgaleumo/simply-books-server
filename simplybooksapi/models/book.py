from django.db import models
from .author import Author

class Book(models.Model):
  
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
  title = models.CharField(max_length=50)
  image = models.ImageField()
  price = models.DecimalField(max_digits=10, decimal_places=4)
  sale = models.BooleanField()
  uid = models.IntegerField()
  description = models.TextField(max_length=150)
