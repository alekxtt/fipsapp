from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/login', views.login_page, name='login'),
    path('profile/logout/', views.logoutUser, name='logout'),
    path('profile/registration', views.user_profile_create, name='profile_create'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/<str:pk>/', views.profile_delete, name='profile_delete'),
]