from django.urls import path
from myapp import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>,/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/',views.delete, name='delete'),
    ]