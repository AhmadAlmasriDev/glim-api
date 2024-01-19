from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'movie',
        
        'owner_name',
        'created_at',
        
        'comment_body',
        'approved',
        )
    list_filter = ('approved', 'created_at')
    search_fields = ('user_name', 'comment_body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
