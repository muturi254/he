from django.contrib import admin
from news.models import Article, Editor, Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Editor)
admin.site.register(Tag)