from django.db import models
from django.contrib.auth.models import User

class Usercontact(models.Model):
    fromID = models.CharField(max_length=50)
    toID = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()

    def summary(self):
        return self.content[:100]  