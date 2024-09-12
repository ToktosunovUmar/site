from django.db import models


class TAG(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CLOTH(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    tags = models.ManyToManyField(TAG)

    def __str__(self):
        return self.name
