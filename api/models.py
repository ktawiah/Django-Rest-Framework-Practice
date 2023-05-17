from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100, blank=True, null=True, unique=True)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_to_complete = models.DateField()

    def __str__(self):
        return self.title


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter_reached = models.IntegerField()
    page_reached = models.IntegerField(null=True)
    next_session = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("user", "book")

    def __str__(self):
        return f"{self.user} -- {self.book}"
