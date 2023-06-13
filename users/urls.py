from django.urls import path
from . import views

urlpatterns = [
    path('admin_login', views.admin_login, name='adminlogin'),
    path('logout_admin', views.logout_admin, name="logoutadmin")
]
