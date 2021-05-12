from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Ebook(models.Model):
    """Create ebook data model"""
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    """Create Books Review data model"""

    ebook = models.ForeignKey(
        Ebook,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return str(self.rating)
