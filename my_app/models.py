from django.db import models
#use django user user model
from django.contrib.auth.models import User

# Create your models here.
#Note model
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # ordering notes in list view with the just created or updated ones
    class Meta:
        ordering = ['-updated', '-created']

    # if a note object is called 50 characters of the title will shown
    def __str__(self):
        return self.title[0:50]