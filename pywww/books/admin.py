from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Book, Author


class BookResource(resources.ModelResource):
    class Meta:
        abstract = True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["id", "title", "publication_year", "avaliable"]
    search_fields = ["title", "author"]
    list_filter = ["avaliable"]
    resource_classes = BookResource
