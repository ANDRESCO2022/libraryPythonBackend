from turtle import title
from django.db import models
from safedelete.models import SafeDeleteModel

# Create your models here.
class Category(SafeDeleteModel):
    name=models.CharField(max_length=150)
    status=models.CharField(max_length=15,default='active')
   
class Author(SafeDeleteModel):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    date_birth=models.DateField
 
class Book(SafeDeleteModel):
    title=models.CharField(max_length=100, null=False)
    topic=models.CharField(max_length=100,)
    date_puplicate=models.CharField(max_length=50)
    status=models.CharField(max_length=15,default='available')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


