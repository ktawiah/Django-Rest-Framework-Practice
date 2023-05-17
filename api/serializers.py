from rest_framework import serializers
from .models import Book, Category, Progress


class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="book-detail")

    class Meta:
        model = Book
        fields = [
            # "user",  # url = serializers.SerializerMethodField(read_only=True)
            "url",
            "id",
            "title",
            "author",
            "category",
            "date_added",
            "date_to_complete",
        ]

    def validate_title(self, data):
        queryset = Book.objects.filter(title_iexact=data)
        if queryset.exists():
            raise serializers.ValidationError(f"{data} already exists.")
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProgressSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="progress-detail")

    class Meta:
        model = Progress
        fields = [
            # "user",
            "url",
            "book",
            "chapter_reached",
            "page_reached",
            "next_session",
            "topic",
            "summary",
        ]

    def validate_chapter_reached(self, data):
        if int(data) < 0:
            raise serializers.ValidationError(
                f"Chapter reached can't be negative. Enter valid chapter"
            )
        return data

    def validate_page_reached(self, data):
        if int(data) < 0:
            raise serializers.ValidationError(
                f"Page number can't be negative. Enter a valid page number."
            )
        return data

    # def validate_topic(self, data):
    #     if len(data) > 10:
    #         return f"{data[:10]}..."

    # def validate_summary(self, data):
    #     if len(data) > 10:
    #         return f"{data[:10]}..."
