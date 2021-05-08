from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.contrib.auth.models import User


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class chiz(models.Model):
    pass

    class Meta:
        verbose_name = 'نمونه'
        verbose_name_plural = 'نمونه ها'


class Articles(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشرشده'),
    )
    title = models.CharField(max_length=100, verbose_name='عنوان ')
    author = models.ForeignKey(User, verbose_name='نویسنده', null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='articles')
    category = models.ManyToManyField('category', verbose_name='دسته بندی', related_name='articles')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله ')
    description = models.TextField(verbose_name=' شرح مقاله')
    thamnail = models.ImageField(upload_to='images', verbose_name='عکس ')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد ')
    updated = models.DateTimeField(auto_now=True, verbose_name=' تاریخ ویرایش')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت نمایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

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

    object = CategoryManager()
