from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class MyVideo(models.Model):
    title = models.CharField(max_length=50, default="NameLess", verbose_name="название")
    slug = models.SlugField(max_length=50, unique=True, help_text="вводи буквы руками")
    description = models.TextField(null=True, blank=True)
    likes = models.PositiveIntegerField(default=0, verbose_name="нравится")
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.slug[:10]}"

    @property
    def player(self):
        return mark_safe(f"<iframe width='100' height='100' src='{self.url}' ></iframe>")


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    video = models.ForeignKey(MyVideo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)