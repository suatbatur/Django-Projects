from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class Student(models.Model):
   name = models.CharField( max_length=100)
   mobile =models.CharField(max_length=20) 
   email =models.CharField(max_length=100)
   GENDER = (
        ("Female" , "Female"),
        ("Male" , "Male"),
        ("Other" , "Other"),
        ("Prefer Not to" , "Prefer Not to"),
    )
   gender = models.CharField(max_length=50, choices=GENDER)
   
   number = models.CharField(max_length=50)
   PATH =(
       ("Front-End", "Front-End"),
       ("Back-End", "Back-End"),
       ("Data Analys", "Data Analys"),
       ("Data Science", "Data Science"),
       ("AWS-DevOps", "AWS-DevOps")
   )
   
   path = models.CharField(max_length=50, choices=PATH)
   
