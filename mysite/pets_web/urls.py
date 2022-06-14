from django.urls import path
from .views import HomeView, PostDetailView, PostAddView, PostUpdateView, DeletePostView, LikeView

app_name = 'pets_web'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post_add/', PostAddView.as_view(), name='post_add'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='post_delete'),
    path('post_like/<int:pk>', LikeView, name='like_post'),
]
