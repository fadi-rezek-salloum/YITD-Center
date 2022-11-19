from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('posts-list/<str:cat>/', views.BlogList.as_view(), name='blogs-list'),
    path('post/<slug>/', views.PostDetails.as_view(), name='post-details'),
]