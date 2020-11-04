from django.db import models
from multiselectfield import MultiSelectField

class CoursesDatabase(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)
    start_time = models.TimeField(max_length=100)
    trainer_name = models.CharField(max_length=100)
    trainer_exp = models.CharField(max_length=100)
    content = models.FileField(upload_to='content', max_length=100)

class FeedbackDatabase(models.Model):
    name = models.CharField(max_length=100)
    ratting = models.IntegerField()
    Date = models.DateTimeField(auto_now_add=True)
    Feedback = models.CharField(max_length=100)

class ContactDatabase(models.Model):
    Name = models.CharField(max_length=100)
    Mobile_Number = models.BigIntegerField()
    Email = models.EmailField(max_length=100)
    COURSES_CHOICES = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Ui', 'Ui'),
        ('Rest Api', 'Rest Api'),
        ('Flask', 'Flask'),
        ('Mysql', 'Mysql'),
    )
    courses = MultiSelectField(max_length=200, choices=COURSES_CHOICES)
    TRAINERS_CHOICES = (
        ('Narayana', 'Narayana'),
        ('Mahesh', 'Mahesh'),
        ('Mohan Reddy', 'Mohan Reddy'),
        ('Srinivas', 'Srinivas'),
        ('Wilson', 'Wilson')
    )
    trainers = MultiSelectField(max_length=200, choices=TRAINERS_CHOICES)
    LOCATIONS_CHOICES = (
        ('Hyd', 'Hyd'),
        ('Bang', 'Bang'),
        ('Pune', 'Pune'),
        ('Delhi', 'Delhi'),
        ('Chennai', 'Chennai')
    )
    locations = MultiSelectField(max_length=200, choices=LOCATIONS_CHOICES)
    SHIFTS_CHOICES = (
        ('Morning', "Morning"),
        ('After Noon', "After Noon"),
        ('Evening', 'Evening'),
        ('Night', 'Night')
    )
    shifts = MultiSelectField(max_length=100, choices=SHIFTS_CHOICES)
    gender = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)

