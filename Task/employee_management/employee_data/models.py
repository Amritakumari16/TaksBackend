# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# ...
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    designation = models.CharField(max_length=32)
