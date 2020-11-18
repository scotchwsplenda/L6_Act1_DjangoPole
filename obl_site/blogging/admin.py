
from django.contrib import admin

from blogging.models import Post, Category, CategoryInLine

# has to have syntactic sugar
#  https://realpython.com/customize-django-admin-python/#modifying-a-change-list-using-list_display
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInLine,)
    list_display = ("title", "created_date")

# has to have syntactic sugar
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)

