from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField(blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
