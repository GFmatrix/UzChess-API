from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

class Rating(BaseModel):
    rating_classic = models.IntegerField()
    last_rating_classic = models.IntegerField()
    rating_rapid = models.IntegerField()
    last_rating_rapid = models.IntegerField()
    rating_blitz = models.IntegerField()
    last_rating_blitz = models.IntegerField()
    place = models.IntegerField()
    last_place = models.IntegerField()

class User(AbstractUser):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True, blank=True)
    country = CountryField()
    pass
