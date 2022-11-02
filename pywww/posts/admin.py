from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Post, Category

class PostResource(resources.ModelResource):
    class Meta:
        abstract = True

@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["id", "author", "title", "created", "modified", "published", "sponsored"]
    search_fields = ["title", "description"]
    list_filter = ["sponsored", "published"]
    resource_class = PostResource

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass