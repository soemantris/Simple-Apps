from django.db import models
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=75, verbose_name="Nama Lengkap")
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
