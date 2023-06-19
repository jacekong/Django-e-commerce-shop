from django.urls import path
from . import views

urlpatterns = [
    path('admin-login', views.admin_login, name='adminlogin'),
    path('logout-admin', views.logout_admin, name="logoutadmin")
]
