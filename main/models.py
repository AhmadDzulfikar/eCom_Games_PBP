import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5