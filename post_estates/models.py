from django.db import models
from django.contrib.auth.models import User


class EstatePost(models.Model):
    apartment = models.CharField(max_length=225)
    images = models.ImageField(upload_to="images/", default="images/fallback.jpg", blank=True)
    location = models.CharField(max_length=78)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    total_package = models.CharField(max_length=78)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="estate_posts"
    )

    def __str__(self):
        return self.apartment
