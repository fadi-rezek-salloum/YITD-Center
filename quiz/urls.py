from django.urls import path

from .import views

app_name = 'quiz'

urlpatterns = [
    path('<str:course_name_en>/', views.getQuiz, name='quiz'),
]