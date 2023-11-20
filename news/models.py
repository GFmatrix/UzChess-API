from django.db import models
from utils.models import BaseModel
from django.utils.translation import gettext_lazy as _



class News(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    views = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)