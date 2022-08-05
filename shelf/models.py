from django.db import models

# Createfrom django.db import models
from safedelete.models import SafeDeleteModel


# Create your models here.
class Shelf(SafeDeleteModel):
    number = models.CharField(null=False, max_length=12)

    def __str__(self):
        return self.number
