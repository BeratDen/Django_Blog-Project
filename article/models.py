from django.db import models
from datetime import datetime
# Create your models here.


class Article(models.Model):
    """Model definition for Article."""

    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=50, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Güncellenme Tarihi')

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
