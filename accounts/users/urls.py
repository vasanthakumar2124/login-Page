from django.urls import path
from .views import home,register_view,Login_view,Logout_view

urlpatterns=[
    path('',home,name='home'),
    path('register/',register_view,name='register'),
    path('login/',Login_view,name='login'),
    path('logout/',Logout_view,name='logout'),
]