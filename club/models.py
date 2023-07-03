from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=100)
    members = models.IntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.comment
