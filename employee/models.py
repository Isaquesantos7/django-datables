from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    job = models.CharField(max_length=160)
    active = models.BooleanField(default=False, blank=True)

    def __Str__(self):
        return self.name