from django.db import models


class RezkaFilm(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='parser/')

    def __str__(self):
        return self.title
