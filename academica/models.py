from django.db import models

# Create your models here.
class IdenticationType(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name



class  Student (models.Model):
    identificationType=models.ForeignKey('IdenticationType',on_delete=models.PROTECT)
    identification=models.CharField(max_length=20)
    name= models.CharField(max_length=100)
    pub_date= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.identification+"-"+ self.name
