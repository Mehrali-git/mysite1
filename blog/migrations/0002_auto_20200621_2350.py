# Generated by Django 3.0.6 on 2020-06-21 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chiz',
            name='family',
        ),
        migrations.RemoveField(
            model_name='chiz',
            name='thamnail',
        ),
    ]
