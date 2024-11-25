from django.urls import path
from example import views

urlpatterns = [
    path('', views.index),
    path('create-table/class/<str:c>/section/<str:s>/year/<str:d>/', views.create_table_view, name='create-table'),
]
