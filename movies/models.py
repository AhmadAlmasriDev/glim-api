from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


RATING = ((0, "G"), (1, "PG"), (2, "PG-13"), (3, "NC-17"), (3, "R"))
STATUS = ((0, "Draft"), (1, "Published"))


class Movie(models.Model):
    Title = models.CharField(max_length=255, blank=False)

    manager = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    rated = models.IntegerField(choices=RATING)
    year = models.IntegerField()
    director = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    distribution = models.CharField(max_length=255, blank=True)
    actors = models.CharField(max_length=255, blank=True)
    poster = CloudinaryField()
    discreption = models.TextField(blank=True)
    price = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
