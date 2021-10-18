from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news-list'),
    path('<int:pk>/detail/', views.NewsDetailView.as_view(), name='news-detail'),
    path('create/', views.NewsCreateView.as_view(), name='news-create'),
    path('<int:pk>/edit/', views.NewsUpdateView.as_view(), name='news-edit'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news-delete'),

    path('commit/create/', views.CommitCreateView.as_view(), name='commit-create'),
]
