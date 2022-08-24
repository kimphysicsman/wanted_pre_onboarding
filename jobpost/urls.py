from django.urls import path
from . import views

# jobpost/
urlpatterns = [
    path('', views.JobPostView.as_view()),
    path('apply/', views.ApplyView.as_view()),
    path('<int:id>/', views.JobPostDetailView.as_view()), 
    path('search/', views.JobPostSearchView.as_view()),
]
