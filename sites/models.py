from django.db import models
from uuid import uuid4

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Site(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True)
    url = models.URLField(max_length=600, unique=True)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-updated',)
