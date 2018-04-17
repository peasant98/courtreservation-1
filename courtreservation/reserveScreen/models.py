from django.db import models

# Create your models here.
class Court(models.Model):
    courtNum=models.IntegerField

    def __str__(self):
        return 'Court'
