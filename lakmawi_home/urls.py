from django.urls import path
from . import views
from .views import HomeView, UploadImage, LikeView, PostDetails, DeletePostView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetails.as_view(), name='post-details'),
    path('upload_image/', UploadImage.as_view(), name='upload-image'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('send_message/', views.send_message, name='send_message'),
    path('delete_post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('search_title/', views.search_title, name="search-title"),
]