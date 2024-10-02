from django.urls import path, include
from.views import login_view, signup_view, logout_view, home_view, admin_login_view, admin_home_view


urlpatterns = [
    path("", home_view, name="home"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("admin_login/", admin_login_view, name="admin_login"),
    path('logout/', logout_view, name='logout'),
    path("admin_home/", admin_home_view, name="admin_home"),
]
