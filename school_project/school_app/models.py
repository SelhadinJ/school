from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256, unique=True)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school_app:detail', kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)
    major = models.CharField(max_length=256)
    dob = models.DateField()
    school = models.ForeignKey(School, related_name='students',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('school_app:list')
