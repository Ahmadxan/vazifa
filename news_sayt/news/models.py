from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class News(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = RichTextField()
    image = models.ImageField(upload_to='images/')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-list')


class Commit(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    message = RichTextField()

    def __str__(self):
        return f"{self.full_name} - {self.news}"

    def get_absolute_url(self):
        return reverse('news-list')