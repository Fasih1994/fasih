# Generated by Django 3.0 on 2020-07-17 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='time',
        ),
    ]
