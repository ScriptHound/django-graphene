from django.db import models
# Create your models here.


class DummyModel(models.Model):
    title = models.TextField(max_length=400)
    body = models.TextField(max_length=1000)
    random_num = models.IntegerField(max_length=10)


