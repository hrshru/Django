from django.urls import path, include
from . import views
from django.contrib.auth.views import password_reset,password_reset_done

app_name = 'social'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('reset_password/',password_reset,name='reset_password'),
    path('reset_password/done/',password_reset_done,name='password_reset_done'),

]
