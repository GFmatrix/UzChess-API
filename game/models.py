from django.db import models
from utils.models import BaseModel
from user.models import User

GAME_TYPES = (
    ('rapid', 'Rapid'),
    ('bullet', 'Bullet'),
    ('blitz', 'Blitz'),
)
class GameType(BaseModel):
    name = models.CharField(max_length=50, choices=GAME_TYPES)
# Create your models here.
class Games(BaseModel):
    player_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_1')
    player_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_2')
    score_1 = models.IntegerField()
    score_2 = models.IntegerField()
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)