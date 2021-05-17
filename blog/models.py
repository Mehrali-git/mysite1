from django.db import models
from django.utils import timezone
from django.urls import reverse
from account.models import User
from django.utils.html import format_html
from extensions.utils import jalali_converter


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Articles(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشرشده'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name='نویسنده')
    title = models.CharField(max_length=100, verbose_name='عنوان ')
    category = models.ManyToManyField('Category', verbose_name='دسته بندی', related_name='articles')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله ')
    description = models.TextField(verbose_name=' شرح مقاله')
    thamnail = models.ImageField(upload_to='images', verbose_name='عکس ')
    is_special = models.BooleanField(default=False, verbose_name='مقاله ویژه')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد ')
    updated = models.DateTimeField(auto_now=True, verbose_name=' تاریخ ویرایش')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت نمایش')

    # is_special = models.BooleanField(default=False, verbose_name='وضعیت نویسندگی')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def thamnail_tag(self):
        return format_html("<img width=120 height=80 style='border-radius:5px' src='{}'/>".format(self.thamnail.url))

    thamnail_tag.short_description = "تصویر"

    def get_absolute_url(self):
        return reverse("account:home")

    def category_to_str(self):
        return " ,".join([category.title for category in self.category.active()])

    category_to_str.short_description = "دسته بندی"

    objects = ArticleManager()


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name='زیردسته')
    title = models.CharField(max_length=100, verbose_name='دسته بندی مقاله')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')
    position = models.IntegerField(verbose_name='جایگاه')

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()
