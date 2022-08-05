import uuid

from django.db import models
from safedelete.models import SafeDeleteModel

from book.models import Book


# Create your models here.
class BookCopy(SafeDeleteModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library",
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
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

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.book}"
