"""
URL configuration for time_tracking_tool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# time_tracking_tool/urls.py

# time_tracking_tool/urls.py

# time_tracking_tool/urls.py

# time_tracking_tool/urls.py

from django.contrib import admin
from django.urls import path, include
from tracker import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', include('tracker.urls')),
    path('', views.homepage, name='homepage'),  # Homepage view
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]



