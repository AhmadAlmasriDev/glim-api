from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from cloudinary.models import CloudinaryField


class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=4)
    owner_name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField(blank=False)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment: {self.comment_body} By: {self.owner_name}"
