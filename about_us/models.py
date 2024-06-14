from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Student(models.Model):
    stu_id = models.IntegerField()
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField(max_length=30)
    
    def __str__(self):
        return f"{self.stu_name} {self.stu_email}"
    