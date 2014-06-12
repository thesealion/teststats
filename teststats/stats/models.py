from django.db import models


class Hit(models.Model):
    user_id = models.IntegerField()
    page_id = models.IntegerField()
    time = models.DateTimeField()
