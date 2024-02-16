from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Like(models.Model):
    movie = models.ForeignKey(
        Movie,
        related_name="likes",
        on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = [["movie", "owner"]]

    def __str__(self):
        return f"Movie: {self.movie} Liked by: {self.owner}"
