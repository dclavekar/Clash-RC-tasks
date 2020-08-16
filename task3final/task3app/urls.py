from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup, name='signup'),
    path('login/',views.views_login, name='login'),
    path('logout/',views.views_logout, name='logout'),
    path('loggedin/',views.views_loggedin, name='loggedin'),
    #path('login/loggedin/',views.views_loggedin, name='login/loggedin'),
    #path('loggedin/logout/',views.views_logout, name='logout'),
    #path('loggedin/logout/login/',views.views_logout, name='logout')

    ]