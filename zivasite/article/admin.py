from ast import Pass
from django.contrib import admin
from article.models import Category, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.title


class CategoryAdmin(admin.ModelAdmin):
    def _str_(self):
        return self.name


class CommentAdmin(admin.ModelAdmin):
    def _str_(self):
        return self.author + self.created_on

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

