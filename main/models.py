import uuid
from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5