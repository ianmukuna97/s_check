from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/analyze/', views.AnalyzeMessageView.as_view()),
    path('api/history/', views.RecentScansView.as_view()),
]
