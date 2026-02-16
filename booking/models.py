from django.db import models

class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def _str_(self):
        return f"Room {self.room_number}"