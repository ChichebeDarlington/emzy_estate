
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EstatePost(models.Model):
    title = models.CharField(max_length=78)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='pics', default='fallback.jpg', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    