from django.db import models

class Author(models.Model):
  email = models.EmailField(max_length=15)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  image = models.URLField(max_length=400)
  favorite = models.BooleanField()
  uid = models.CharField(max_length=50)
