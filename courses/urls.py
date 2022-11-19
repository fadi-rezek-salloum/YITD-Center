from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('details/<pk>/', views.CourseDetails.as_view(), name='course_details'),
    path('details/<pk>/request', views.RequestCourse.as_view(), name='course_request')
]
