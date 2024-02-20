from django.db import models

class Info(models.Model):
    name = models.TextField(default='name')
    email = models.EmailField(default='example@example.com')  # Provide a suitable default email
    subject = models.CharField(default='nepal',max_length=255)
    message = models.TextField(default ='how are you')

    def __str__(self):
        return self.name
