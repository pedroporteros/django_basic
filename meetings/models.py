
from datetime import time
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()
    
    def __str__(self):
        return f"{self.name}, floor {self.floor_number}, room number {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    participants = models.ManyToManyField(get_user_model())
    
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
    
