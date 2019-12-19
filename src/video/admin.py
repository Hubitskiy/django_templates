from django.contrib import admin
from .models import MyVideo, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2
    readonly_fields = ['likes']


class MyVideoAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title', 'date', 'likes', 'player']
    #exclude = ['likes']
    readonly_fields = ['likes']
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(MyVideo, MyVideoAdmin)