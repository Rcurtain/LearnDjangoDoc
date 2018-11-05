from django.db import models
from django.utils import dates

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return "".join(["<Person:>", self.name])


class Group(models.Model):
    name = models.CharField(max_length = 128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

    
class Membership(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_jioned = models.DateField()
    invite_reason = models.CharField(max_length = 64)