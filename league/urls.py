from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.teams, name='teams'),
    path('add_team/', views.add_team, name='add_team'),
    path('delete_team/<int:team_id>/', views.delete_team, name='delete_team'),
    path('results/', views.results, name='results'),
    path('show_round/<int:round_id>/', views.show_round, name='show_round'),
]