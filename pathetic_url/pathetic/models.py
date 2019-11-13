from django.db import models


class Url(models.Model):
    long_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    visited = models.PositiveIntegerField(default=0)
