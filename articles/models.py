from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title
