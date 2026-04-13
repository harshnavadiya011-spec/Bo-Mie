from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.JSONField()
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.name