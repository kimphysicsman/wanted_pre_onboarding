from django.urls import path
from . import views

# jobpost/
urlpatterns = [
    path('', views.JobPostView.as_view()),
    path('<id>/', views.JobPostDetailView.as_view()), 
]
