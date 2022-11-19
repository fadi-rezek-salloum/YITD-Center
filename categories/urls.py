from django.urls import path

from . import views

app_name = 'category'

urlpatterns = [
    path('<slug>/', views.CategoryDetails.as_view(), name='category_details'),
]
