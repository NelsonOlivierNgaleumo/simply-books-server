from django.db import models

class Author(models.Model):
  email = models.EmailField(max_length=15)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  image = models.ImageField()
  favorite = models.BooleanField()
  uid = models.PositiveIntegerField()
