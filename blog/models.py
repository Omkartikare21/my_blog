from django import core
from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=18)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=80)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Posts(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=200)
    # height_field=500, width_field=500, max_length=None,  --> these r extra fields in imagefield
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_name = models.CharField(max_length=80)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Posts, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name_plural = "Comments"
