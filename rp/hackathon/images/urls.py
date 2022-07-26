from django.urls import path

from .views import PostDeleteView, PostUpdateView, postImage, PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('show/<int:pk>/', PostDetailView.as_view(), name="image-detail"),
    path('new/', postImage, name='post-create'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
]
