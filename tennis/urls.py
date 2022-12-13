from django.urls import path

from . import views

app_name = 'tennis'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('match/<int:pk>/', views.match, name='match'),
    #path('equipe_choice/ligue_choice/<int:id>/match/', views.match, name='match'),
]