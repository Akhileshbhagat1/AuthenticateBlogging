# Generated by Django 2.2.2 on 2020-01-25 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200125_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
    ]
