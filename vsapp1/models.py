from django.db import models

class Person(models.Model):
    name = models.TextField()
    gender = models.IntegerField()
    fav = models.IntegerField()
    image = models.ImageField(blank = True)
    degree = models.IntegerField()
    played = models.IntegerField()
    won = models.IntegerField()

    def __str__(self):
        return self.name

class Adjective(models.Model):
    phrase = models.TextField()
    gender = models.IntegerField()
    fav = models.IntegerField()
    degree = models.IntegerField()
    played = models.IntegerField()
    won = models.IntegerField()

    def __str__(self):
        return self.phrase