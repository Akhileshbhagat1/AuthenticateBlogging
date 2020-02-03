# Generated by Django 2.2.2 on 2020-01-25 03:48
import os
from django.db import migrations
from django.conf import settings
from django.contrib.auth.hashers import make_password


def backfill_users(apps, schema_editor):
    password = os.getenv('LEGACY_USER_PASSWORD')

    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User.objects.create(
        username='legacy',
        email='legacy@example.com',
        is_active=False
    )
    user.password = make_password(password)
    user.save()

    Blogpost = apps.get_model('blog', 'BlogPost')
    for post in Blogpost.objects.filter(user=None):
        post.user = user
        post.save()


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_blogpost_user'),
    ]

    operations = [
        migrations.RunPython(backfill_users),
    ]
