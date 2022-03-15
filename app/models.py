from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_type=models.CharField(max_length=10,default=2,choices=(('1','employe'),('2','worker')))
    mobile_number=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.username
        
class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    note_name=models.CharField(max_length=100)
    note_describe=models.TextField(max_length=1000)
    note_date=models.DateField(auto_now_add=True)
    
   
    