from django.db import models

# Create your models here.


class Chatroom(models.Model):
    chatroom_id = models.AutoField(
        db_column='chatroom_id',
        primary_key=True)

    name = models.CharField(max_length=20, blank=False)
    subject = models.CharField(max_length=145, blank=False)

    def __str__(self):
        return self.name
