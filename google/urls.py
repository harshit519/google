"""
URL configuration for google project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirect allauth login to custom login
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=True)),
    path('accounts/signup/', RedirectView.as_view(url='/signup/', permanent=True)),
    
    # Custom authentication URLs
    path('', include('google_login.urls')),
    
    # Django allauth URLs (for OAuth callback handling only)
    path('accounts/', include('allauth.urls')),
]
