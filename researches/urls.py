from django.urls import path

from . import views

app_name = 'researches'

urlpatterns = [
    path('list/<str:cat_name>/', views.ResearchesList.as_view(), name='researches-list'),
    path('<slug>/', views.ResearchDetails.as_view(), name='research-details'),
]
