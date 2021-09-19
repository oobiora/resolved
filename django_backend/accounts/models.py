from django.db import models
from .resources import languages, countries
# Create your models here.
class User(models.Model):
    LANGUAGE_SELECT = languages
    COUNTRY_SELECT = countries
    username = models.CharField(max_length=255, unique=True, blank=False)
    real_name = models.CharField(max_length=50, unique=False, blank=False)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_SELECT, default='en', null=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRY_SELECT, default="US", null=True, blank=True)
    verified = models.BooleanField(default=False)
    joined = models.DateField(auto_now_add=True)
    action_steps = models.ManyToManyField(
        'services.Action',
        related_name="u_action",
        related_query_name="u_actions",
        blank = True
    )
    


