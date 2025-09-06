from django.urls import path
from google_login import views
urlpatterns = [
    
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('signup/', views.signup, name='signup'),
    path('data', views.data, name='data'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('logout/confirm/', views.logout_confirm, name='logout_confirm'),
   

    
    
    
    ]
