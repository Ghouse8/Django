from django.db import models

# Create your models here.
class Post(models.Model):
    text=models.TextField()
    # We are defining this string for displaying the name for the above 'text' object.
    def __str__(self):
        """A string representation of the model"""
        return self.text[:50]
