"""job_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from job_portal_app import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/',views.register),
    path('index/',views.index),
    path('login/',auth_view.LoginView.as_view(template_name='login.html')),
    path('logout/',auth_view.LogoutView.as_view()),

    # IT JOB CODE

    path('add/',views.add),
    path('read/',views.read),
    path('delete/<int:id>/',views.delete),
    path('update/<int:id>/',views.update),

    # MECH JOB CODE
    path('read_mech/',views.read_mech),
    path('add_mech/',views.add_mech),
    path('update_mech/<int:id>/',views.update_mech),
    path('delete_mech/<int:id>/',views.delete_mech),

    # CIVIL JOB CODE
    path('read_civil/',views.read_civil),
    path('add_civil/',views.add_civil),
    path('update_civil/<int:id>/',views.update_civil),
    path('delete_civil/<int:id>/',views.delete_civil),
]
