from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie

SEATS = 84


class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.IntegerField(
        validators=[MaxValueValidator(SEATS), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    show_date = models.DateField()
    reserve = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner} movie: {self.movie} at: {self.show_date}"
