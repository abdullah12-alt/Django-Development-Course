from django.db import models
from django.utils import timezone
# Create your models here.
class PostTable(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    created_at=models.DateTimeField(timezone.now())
 