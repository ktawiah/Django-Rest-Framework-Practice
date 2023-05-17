from rest_framework import serializers
from .models import Book, Category, Progress


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "user",
            "id",
            "title",
            "author",
            "category",
            "date_added",
            "date_to_complete",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = [
            "user",
            "book",
            "chapter_reached",
            "page_reached",
            "next_session",
            "topic",
            "summary",
        ]
