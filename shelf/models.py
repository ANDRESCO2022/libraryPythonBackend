from django.db import models

# Createfrom django.db import models
from safedelete.models import SafeDeleteModel

# Create your models here.
class Self(SafeDeleteModel):
    pass
