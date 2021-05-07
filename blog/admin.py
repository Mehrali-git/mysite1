from django.contrib import admin
from . import models


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


make_published.short_description = 'تغییر وضعیت موارد ازپیش نویس به انتشار'


def make_draft(a, b, c):
    c.update(status='d')


make_draft.short_description = 'تغییر وضعیت موارد ازانتشار به پیش نویس'


@admin.register(models.chiz)
class chizAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'jpublish', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return " ,".join([category.title for category in obj.category_published()])

    category_to_str.short_description = "دسته بندی"


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
