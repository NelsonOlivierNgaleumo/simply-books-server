from django.db import models
from .author import Author

class Book(models.Model):
  
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
  title = models.CharField(max_length=50)
  image = models.URLField(max_length=400)
  price = models.DecimalField(max_digits=10, decimal_places=4)
  sale = models.BooleanField()
  uid = models.CharField(max_length=50)
  description = models.CharField(max_length=150)
