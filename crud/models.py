from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    organisation = models.CharField(max_length=50, default="HNGX")
    role = models.CharField(max_length=20, default="intern")

    def __str__(self) -> str:
        return self.name
