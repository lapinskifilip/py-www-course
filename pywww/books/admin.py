from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Book, Author


class BookResource(resources.ModelResource):
    class Meta:
        abstract = True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ["id", "title", "publication_year", "avaliable"]
    search_fields = ["title", "author"]
    list_filter = ["avaliable"]
    resource_classes = BookResource
