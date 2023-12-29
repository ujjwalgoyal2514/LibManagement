from django.db import models
class BookStore(models.Model):
    bookid=models.CharField(max_length=15,primary_key=True)
    isbno=models.CharField(max_length=15)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    bookname=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    qty=models.PositiveIntegerField()

class IssueBook(models.Model):
    bookid=models.CharField(max_length=15)
    isbno=models.CharField(max_length=15)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    bookname=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    rollno=models.IntegerField()
    name=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    issuedate=models.CharField(max_length=30)
    duedate=models.CharField(max_length=30)
    status=models.CharField(max_length=20)

class Program(models.Model):
    program=models.CharField(max_length=100)
class Branch(models.Model):
    branch=models.CharField(max_length=100)
class Year(models.Model):
    year=models.CharField(max_length=100)
    
    

# Create your models here.
