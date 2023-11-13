from django.db import models
from django.contrib.auth.models import User



RATING = ((0, "G"), (1, "PG"), (2, "PG-13"), (3, "NC-17"), (3, "R"))
STATUS = ((0, "Draft"), (1, "Published"))


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False)
    manager = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=4)
    manager_name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    rated = models.IntegerField(choices=RATING)
    year = models.IntegerField()
    director = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    distribution = models.CharField(max_length=255, blank=True)
    actors = models.CharField(max_length=255, blank=True)
    poster = models.ImageField(upload_to="images/", default="../default_post_jneohh")
    discreption = models.TextField(blank=True)
    price = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
