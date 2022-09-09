from django.db import models

# Create your models here.
from base.models import Base
from user.models import User


class Log(Base):
    class Meta:
        ordering = ('-created_at',)

    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    request = models.JSONField(null=True, blank=True)
    response = models.JSONField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    status = models.CharField(null=True, blank=True, max_length=255)
    headers = models.JSONField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.id}"