from django.db import models
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
        return self.full_name
        
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class My_Info(models.Model):
    first_name =  models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
