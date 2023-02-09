from django.db import models


class Post(models.Model):
    cost = models.IntegerField(default=30000)

    def __str__(self):
        return str(self.cost)
