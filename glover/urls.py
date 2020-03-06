from django.urls import path

from . import views

app_name = "glover"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('discover/', views.discover, name='discover'),
    path('discover/<str:username>/', views.discover_profile, name='discover_profile'),
    path('matches/', views.matches, name='matches'),
    # path('matches/<str:username>/', views.matches_profile, name='matches-profile'),
    # path('dms/', views.dms, name='dms'),
    path('profile/', views.profile, name='profile'),
    # path('profile/edit/', views.edit_profile, name='edit-profile'),
]