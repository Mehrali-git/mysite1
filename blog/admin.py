from django.contrib import admin
from . import models


# admin.site.disable_action('delete_selected')

def make_published(modeladmin, request, queryset):
    row_updated = queryset.update(author=2)
    if row_updated == 1:
        message = "منتشرشد"
    else:
        message = "منتشرشدند"
    modeladmin.message_user(request, "{} مقاله {}".format(row_updated, message))


make_published.short_description = "انتشار مقالات انتخاب شده"


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"


def make_Category_enable(modeladmin, request, queryset):
    queryset.update(status=True)


make_Category_enable.short_description = 'نمایش دسته های انتخاب شده'


def make_Category_disable(modeladmin, request, queryset):
    queryset.update(status=False)


make_Category_disable.short_description = 'عدم نمایش دسته های انتخاب شده'


@admin.register(models.chiz)
class chizAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'thamnail_tag', 'status', 'jpublish', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']
    actions = [make_published, make_draft]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_Category_enable, make_Category_disable]
