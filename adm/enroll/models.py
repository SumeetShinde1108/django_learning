from django.db import models

class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.CharField(max_length=70)
    stupass=models.CharField(max_length=70)
    def __str__(self):
        return self.stuname

    '''for printing integer, wrapped it in a str()
    def __str__(self):
        return str(self.stuid)''' 

  