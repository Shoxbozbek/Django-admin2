from django.db import models

class Home(models.Model):
    
    login = models.CharField(max_length=80)
    login2 = models.CharField(max_length=80)
    login3 = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    text = models.CharField(max_length=200)
    text2 = models.CharField(max_length=200)
    logo = models.CharField(max_length=80)
    
    def __str__(self):
        return self.logo