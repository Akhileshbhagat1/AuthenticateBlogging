from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=100)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # author = models.CharField(max_length=100, db_index=True)
    body = models.TextField()

    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def author(self):
        return self.user.username
