from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100, default="BCA")
    semester = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username