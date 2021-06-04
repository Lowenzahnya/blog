from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('article/<int:pk>/', views.detail, name='detail'),
    path('article/<int:pk>/comment', views.comment, name='comment'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]
