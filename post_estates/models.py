from django.db import models
from django.contrib.auth.models import User


class EstatePost(models.Model):
    title = models.CharField(max_length=78)
    images = models.ImageField(upload_to="images/", default="images/fallback.jpg", blank=True)

    details = models.CharField(max_length=255)
    location = models.CharField(max_length=78)

    price = models.PositiveIntegerField()

    house_type = models.CharField(max_length=78)

    bedroom = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    toilet = models.PositiveIntegerField()

    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="estate_posts"
    )

    def __str__(self):
        return self.title
