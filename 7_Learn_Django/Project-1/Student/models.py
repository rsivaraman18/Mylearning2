from django.db import models

class Mystudent(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=40,null=True)
    pay = models.FloatField(default=0)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.designation}'

