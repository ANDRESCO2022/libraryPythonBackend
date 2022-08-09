import uuid

from django.db import models
from safedelete.models import SafeDeleteModel

from book.models import Book
from users.models import UserLibrary


# Create your models here.
class BookCopy(SafeDeleteModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    LOAN_STATUS = (
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="a",
        help_text="Book availability",
    )

    def __str__(self):

        return f"{self.book}"


class BookCopyLybrary(SafeDeleteModel):
    library = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    userBook = models.ForeignKey(UserLibrary, on_delete=models.CASCADE)
    due_back = models.DateField(max_length=100, null=True, blank=True)

    LOAN_STATUS = (
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="a",
        help_text="Book availability",
    )

    def __str__(self):

        return f"{self.book}"
