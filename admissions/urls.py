from django.urls import path

from . import views

app_name = 'admissions'

urlpatterns = [
    path('list/', views.AdmissionsList.as_view(), name='admissions-list'),
    path('<slug>/', views.AdmissionDetails.as_view(), name='admission-details'),
]
