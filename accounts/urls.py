from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView ,logoutView,MyLoginView

app_name = 'accounts'
urlpatterns =[
    path("", include("django.contrib.auth.urls")),
    path('login/', MyLoginView.as_view(), name='login'), 
    path('logOut/',logoutView, name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),


]