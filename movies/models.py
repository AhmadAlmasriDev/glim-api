from django.db import models
from django.contrib.auth.models import User
from datetime import date


RATING = ((0, "G"), (1, "PG"), (2, "PG-13"), (3, "NC-17"), (3, "R"))
STATUS = ((0, "Draft"), (1, "Published"))


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False)
    trailer = models.CharField(max_length=255, blank=True)
    manager = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=4)
    manager_name = models.CharField(max_length=255,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    session_time = models.TimeField()
    rated = models.IntegerField(choices=RATING,  default=0)
    year = models.IntegerField(default=int(date.today().year))
    director = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    distribution = models.CharField(max_length=255, blank=True)
    actors = models.CharField(max_length=255, blank=True)
    poster = models.ImageField(
        upload_to="images/",
        default="../default_post_jneohh")
    discreption = models.TextField(blank=True)
    price = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
