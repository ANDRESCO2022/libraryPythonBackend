from django.db import models
from safedelete.models import SafeDeleteModel

from shelf.models import Shelf

# from book_copy.models import BookCopy


# Create your models here.
class Category(SafeDeleteModel):
    name = models.CharField(max_length=150)
    category_status = [
        ("active", "active"),
        ("inactive", "inactive"),
    ]
    status = models.CharField(max_length=15, choices=category_status, default="ac")


def __str__(self):
    return self.name


class Author(SafeDeleteModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name,self.last_name}"


class Book(SafeDeleteModel):
    title = models.CharField(max_length=100, null=False)
    topic = models.CharField(
        max_length=100,
    )
    date_puplicate = models.DateField()
    book_status = [
        ("avalible", "avalible"),
        ("occupied", "occupied"),
    ]
    status = models.CharField(max_length=15, choices=book_status, default="avalible")
    # numCopies = models.CharField(max_length=100, null=False)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # book_copy = models.ForeignKey(BookCopy,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
