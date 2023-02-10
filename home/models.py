from django.db import models


class Post(models.Model):
    cost = models.IntegerField(default=30000, verbose_name='هزینه پست ارسالی')

    class Meta:
        verbose_name = 'هزینه پست'
        verbose_name_plural = 'هزینه پست'

    def __str__(self):
        return str(self.cost)
