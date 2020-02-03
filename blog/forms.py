from django import forms
from blog.models import BlogPost
from django.contrib.auth.models import User


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'published']


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self):
        user = super(UserSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
