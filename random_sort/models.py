from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chamber(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    picture = models.ImageField()

    def __str__(self):
        return f"{self.name} - {self.person}"