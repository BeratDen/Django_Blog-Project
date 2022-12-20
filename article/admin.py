from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "updated_at"]
    list_display_links = ["title", "created_at", "updated_at"]

    search_fields = ["title", "author__username"]

    list_filter = ["created_at", "title", "author"]

    class Meta:
        model = Article
