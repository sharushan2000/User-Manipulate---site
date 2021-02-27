from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.index ,name='index'),
    path('contact',views.contact , name='contact'),
    path('about',views.about ,name ='about'),
    path('register/',views.register , name='register'),
    path('rsrc',views.resource , name='resource'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
]
