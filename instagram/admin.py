from django.contrib import admin
from .models import Comment, Post
from django.contrib.auth.admin import UserAdmin

class StyledComment(UserAdmin):
    list_display = ('user', 'post', 'body', 'date_posted')
    filter_horizontal = ()
    fieldsets = ()
    ordering = ('-post',)
    list_filter = ()

class StylePost(UserAdmin):
    list_display = ('user', 'image', 'description', 'date_posted')
    filter_horizontal = ()
    fieldsets = ()
    ordering = ('-date_posted',)
    list_filter = ()
# Register your models here.
admin.site.register(Comment, StyledComment)
admin.site.register(Post, StylePost)