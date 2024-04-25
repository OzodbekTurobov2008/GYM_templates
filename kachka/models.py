from django.db import models

#Trainers

class Trainer(models.Model):
    full_name = models.CharField(max_length=125)
    image = models.ImageField(upload_to="Trainer/")
    facebook = models.CharField(max_length=70)
    twitter = models.CharField(max_length=70)
    instagram = models.CharField(max_length=70)
    
    def __str__ (self):
        return self.full_name
    
class Contact(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    
    def __str__ (self):
        return self.name
    
    