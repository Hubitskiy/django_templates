from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from datetime import date


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
    
    @property
    def comment(self):
        return self.comment_set.all()
    
    @property
    def long_post(self):
        return date.today() - self.date.date()

    def to_json(self):
        return {"title":self.title,
                "slug":self.slug,
                "description":self.description,
                "likes":self.likes,
                "url":self.url,
                "date":self.date,
                "comment":self.comment,
                "long_post":self.long_post}


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    video = models.ForeignKey(MyVideo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text[:20]