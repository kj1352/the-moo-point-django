from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20, blank=False)
    usn = models.CharField(max_length=10, blank=False)
    topic = models.CharField(blank = True, max_length=100)
    title = models.CharField(max_length=200, blank=False)
    text = tinymce_models.HTMLField(blank=False)

    def __str__(self):
        return self.title
