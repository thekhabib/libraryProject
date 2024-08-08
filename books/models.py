from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def clean(self):
        super().clean()
        if len(self.isbn) != 13 or not self.isbn.isdigit():
            raise ValidationError('ISBN must be 13 digits')

    def __str__(self):
        return self.title
