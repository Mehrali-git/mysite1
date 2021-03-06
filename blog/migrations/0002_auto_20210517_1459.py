# Generated by Django 3.2 on 2021-05-17 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان ')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله ')),
                ('description', models.TextField(verbose_name=' شرح مقاله')),
                ('thamnail', models.ImageField(upload_to='images', verbose_name='عکس ')),
                ('is_special', models.BooleanField(blank=True, default=False, null=True, verbose_name='مقاله ویژه')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد ')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=' تاریخ ویرایش')),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشرشده')], max_length=1, verbose_name='وضعیت نمایش')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='دسته بندی مقاله')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')),
                ('position', models.IntegerField(verbose_name='جایگاه')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.category', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی مقاله',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.DeleteModel(
            name='chiz',
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
