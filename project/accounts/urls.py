from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),               
    path ('register/' , views.register ,name  = 'register'),    
    path ('login/' , auth_views.LoginView.as_view(template_name = 'login.html') , name = 'login'),
    path ('logout/', auth_views.LogoutView.as_view (), name = 'logout'),
    path('dashboard/', views.dashboard , name= 'dashboard'),
]

