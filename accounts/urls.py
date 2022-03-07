from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('activate-account/<uid>/<token>/', views.activate_account, name='activate'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile')
]
