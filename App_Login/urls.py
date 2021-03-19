from django.urls import path
from . import views

app_name = 'App_Login'
urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.user_change, name='change_profile'),
    path('password/', views.pass_change, name='change_pass'),
    path('pic_add/', views.pic_add, name='pic_add'),
    path('pic_change/', views.pic_change, name='pic_change')

]
