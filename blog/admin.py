from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'published_at')
    raw_id_fields = ('likes',)
    list_display = ('title', 'author', 'published_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text')
    raw_id_fields = ('post', 'author')
