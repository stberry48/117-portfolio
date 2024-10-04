from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='static/img')
    repository = models.URLField()
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return f"{self.name} - ({self.year})"

class Experience(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    skills = models.ManyToManyField(Skill)
    
    def __str__(self):
        return self.name