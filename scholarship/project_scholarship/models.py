from django.db import models

class extenduser(models.Model):
    STATUS = (
    ("PENDING", "PENDING"),
    ("ENROLLED", "ENROLLED"),
    )

# Create your models here.
