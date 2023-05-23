import uuid
from django.db import models



class TimeStampedModel(models.Model):
    id = models.CharField(max_length=32,primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True