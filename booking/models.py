from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

GUESTS = (
    ("1 guest", "1 guest"),
    ("2 guests", "2 guests"),
    ("3 guests", "3 guests"),
    ("4 guests", "4 guests"),
    ("5 guests", "5 guests"),
    ("6 guests", "6 guests"),
    ("7 guests", "7 guests"),
    ("8 guests", "8 guests"),
    )
TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
    ("9 PM", "9 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guests = models.CharField(max_length=50, choices=GUESTS)
    First_name = models.CharField(max_length=20, help_text='First name')
    Last_name = models.CharField(max_length=20, help_text='Last name')
    Email = models.EmailField(max_length=20, help_text='Email')
    Phone = models.CharField(max_length=20, help_text='Phone')
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time} | First_name: {self.First_name}| Last_name: {self.Last_name}| Email: {self.Email}| Phone: {self.Phone}"
