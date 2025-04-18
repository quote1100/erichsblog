from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView
)
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('posts/', PostListView.as_view(), name="blog-posts"),

    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog-posts-detail"),
    path('rpcoff/', views.rpcoff, name="blog-rpcoffline"),
    path('rpconline/', views.rpconline, name="blog-rpconline"),
    path('tfproject/', views.tfproject, name="blog-tensorflow"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
