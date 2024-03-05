from django.db import models
# Create your models here.
class cab(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
class Hotels(models.Model):
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    image=models.CharField(max_length=100000,null=True)
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100,null=True)
    bussiness_registration=models.IntegerField(null=True)
    rating=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class places(models.Model):
    place_name=models.CharField(max_length=100)
    place_desc=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    pimage=models.CharField(max_length=100000,null=True)
    def __str__(self):
        return self.place_name
class lodge(models.Model):
    name=models.CharField(max_length=100)
    contacts=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    typeOfroom=models.CharField(max_length=100)
    total_rooms=models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.name
