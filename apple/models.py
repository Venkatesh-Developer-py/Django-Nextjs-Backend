from django.db import models

class Employedetails(models.Model):
    Employe_name = models.CharField(max_length=50)
    Employe_age = models.CharField(max_length=50)
    Employe_gender = models.CharField(max_length=50)
    Employe_designation = models.CharField(max_length=50)
    Employe_salary = models.CharField(max_length=50)
    Employe_number = models.CharField(max_length=50)

    def __str__(self):
        return self.Employe_name
# Create your models here.