from django.urls import path

from . import views


urlpatterns = [
    path('', views.GreetingView.as_view(), name='greeting'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('index/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('index/create/', views.CreateView.as_view(), name='create'),
    path('index/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
