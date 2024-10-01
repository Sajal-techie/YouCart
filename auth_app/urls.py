from django.urls import path, include
from.views import login_view, signup_view, logout_view, home_view


urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path("", home_view, name="home"),
]
