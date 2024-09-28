from django.db import models

class UserData(models.Model):
    name=models.CharField(max_length=70)
    contact=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


