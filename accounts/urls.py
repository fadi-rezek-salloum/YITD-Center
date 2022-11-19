from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/<pk>/', views.UpdateUserView.as_view(), name='profile'),
]
