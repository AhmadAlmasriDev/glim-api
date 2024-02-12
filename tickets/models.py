from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie

# from datetime import timedelta
# from django.db.models.functions import Now

SEATS = 84

class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.IntegerField( validators=[MaxValueValidator(SEATS), MinValueValidator(1)] )
    created_at = models.DateTimeField(auto_now_add=True)
    show_date = models.DateField()
    reserve = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner} movie: {self.movie} at: {self.show_date}"
    

# def deletes_in_ten_seconds(self):
#     time = self.created_at + timedelta(seconds=10)
#     query = Ticket.objects.get(pk=self.pk)
    
    
#     while True:
#         if time > now():
#             query.delete()
#             break