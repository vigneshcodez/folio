from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Technologies(models.Model):
    name = models.CharField(max_length=25,null=False,blank=False)
    # line2 = models.CharField(max_length=25,null=False,blank=False)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
    
class Services(models.Model):
    name  = models.CharField(max_length=25,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="serviceimages/")

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=40,null=False,blank=True)
    image = models.ImageField(upload_to="projectimages/")
    description = models.CharField(max_length=40,null=True,blank=True)
    explanation = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Myprofile(models.Model):
    name = models.CharField(max_length=40,null=False,blank=False)
    description = models.TextField()
    about = models.TextField()
    image = models.ImageField(upload_to="profileimages/")

    facebook = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    github = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)

    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Enquiry(models.Model):
    name = models.CharField(max_length=40,null=False,blank=False)
    email = models.CharField(max_length=50,null=False,blank=False)
    mobile = models.CharField(max_length=10,null=False,blank=False)
    message = models.TextField(null=False,blank=False)



