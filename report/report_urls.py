

from django.urls import path
from . import views


app_name= 'report'
urlpatterns = [
    path('', views.TrackReport, name = 'track_report'),
    path('input/', views.TrackInput, name = 'track_input'),
    path('update/<int:pk>/', views.TrackUpdate.as_view(), name = 'track_update'),
    path('delete/<int:pk>/', views.TrackDelete.as_view(), name = 'track_delete'),
    path('data_export/', views.export_data_csv, name = 'track_data_export'),

]
