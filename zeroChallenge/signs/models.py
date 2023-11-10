from django.db import models


class Sign(models.Model):
    adress = models.CharField(max_length=200)
    classification = models.TextField()
    view = models.TextField()
    solved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}. {self.title}'