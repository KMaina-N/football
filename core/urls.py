from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_team/', views.add_team, name='add_team'),
    path('delete_team/<int:pk>', views.delete_team, name='delete_team'),
    path('edit/<int:pk>', views.edit_team, name='edit')
]