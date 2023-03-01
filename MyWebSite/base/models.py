from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.email
