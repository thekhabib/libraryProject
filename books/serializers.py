from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "The title must contain letters!",
                }
            )
        isbn = data.get('isbn', None)
        # if not isbn.isdigit() or len(isbn) != 13:
        #     raise ValidationError(
        #         {
        #             'status': False,
        #             'message': "ISBN must be 13 digits!",
        #         }
        #     )
        if Book.objects.filter(title=title, isbn=isbn).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': "This book has already been added!",
                }
            )
        return data
