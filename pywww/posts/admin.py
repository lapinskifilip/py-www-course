from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "title", "created", "modified", "published", "sponsored"]
    search_fields = ["title", "description"]
    list_filter = ["sponsored", "published"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass