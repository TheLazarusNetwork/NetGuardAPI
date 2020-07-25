from django.urls import re_path
from . import views


urlpatterns = [
    re_path('createNetGuard/$', views.CreateNewGuardView.as_view()),
    re_path('getNetGuard/', views.GetNetGuardView.as_view()),
]