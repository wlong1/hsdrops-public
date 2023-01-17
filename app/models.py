from django.db import models

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    publish_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

