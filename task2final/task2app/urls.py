from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.page1, name='page1'),
    path('page2/', views.page2, name= 'page2')


]