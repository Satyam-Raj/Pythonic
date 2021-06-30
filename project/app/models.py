from django.db import models


class Student(models.Model):
    class Gender(models.TextChoices):
        choose = 'select', ('choose')
        male = 'M', ('Male')
        female = 'F', ('Female')


    name        =       models.CharField(max_length= 100)
    age         =       models. IntegerField()
    email       =       models.EmailField(max_length=100)
    gender      =       models.CharField(
        max_length=50,
        choices = Gender.choices,
        default = Gender.choose, )
