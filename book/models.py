from turtle import title
from django.db import models
from safedelete.models import SafeDeleteModel

# Create your models here.
class Book(SafeDeleteModel):
    title=models.CharField(max_length=100, null=False)
    subject=models.CharField(max_length=100,)
    category=models.CharField(max_length=100, )
    data_puplicate=models.CharField(max_length=50)
