from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applications/', views.application_list, name='application_list'),
    path('add-application/', views.add_application, name='add_application'),
    path(
    'edit-application/<int:pk>/',
    views.edit_application,
    name='edit_application'
),
    path(
    'delete-application/<int:pk>/',
    views.delete_application,
    name='delete_application'
),
path(
    'dashboard/',
    views.dashboard,
    name='dashboard'
),
path(
    'logout/',
    views.user_logout,
    name='logout'
),
path(
    'register/',
    views.register,
    name='register'
),
path(
    'export-csv/',
    views.export_csv,
    name='export_csv'
),
]