from django.db import models

# Create your models here.
class house(models.Model):
    price=models.FloatField()
    sf=models.FloatField()
    location=models.TextField()
    bhk=models.IntegerField()
    # furnished status
    furn_status=models.TextField()
    age_of_prop=models.IntegerField()
    # types of properties
    ty_of_prop=models.TextField()
    gender=models.TextField()
