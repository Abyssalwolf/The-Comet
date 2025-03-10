from django.urls import path
from . import views
from .views import custom_logout

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', custom_logout, name='logout'),
]