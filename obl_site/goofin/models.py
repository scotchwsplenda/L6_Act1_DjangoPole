from django.db import models
from django.contrib.auth.models import User

class Goof_Table(models.Model):
    goof_name = models.CharField(max_length=128)
    goof_thot = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    goof_score = models.IntegerField(default=0)

    def __str__(self):
        return self.goof_name