from django.db import models
class StuResponse(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=50)
    program=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.EmailField(max_length=50)
    responsetype=models.CharField(max_length=50)
    subject=models.CharField(max_length=500)
    responseText=models.CharField(max_length=1000)
    responsedate=models.CharField(max_length=30)


# Create your models here.
