from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostInline(admin.TabularInline):
    model = Post.tags.through
    raw_id_fields = ['post', ]


class CommentsInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['author', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'published_at')
    raw_id_fields = ('likes',)
    list_display = ('title', 'author', 'published_at')
    inlines = [CommentsInline, ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.prefetch_related('comments')
        return qs

    def comments(self, obj):
        return obj.comments.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [PostInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text')
    raw_id_fields = ('post', 'author')
