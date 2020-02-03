from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('posts/', views.BlogPostView.as_view(), name='posts'),
    path('posts/<int:id>/', views.BlogPostDetailView.as_view(), name='posts-detail'),
    path('posts/create/', views.BlogPostCreateView.as_view(), name='posts-create'),
    path('posts/<int:id>/edit/', views.BlogPostEditView.as_view(), name='posts-edit'),
    path('accounts/signup/', views.SignupView.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='blog/login.html', next_page='/accounts/login'), name='logout'),


]
