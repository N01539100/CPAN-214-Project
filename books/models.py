from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()
    posted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
