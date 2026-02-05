from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    cv = models.FileField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='certificates/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200, default='N/A')
    gpa = models.CharField(max_length=10)
    start_year = models.IntegerField()
    end_year = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return self.university

