from django.urls import path
from .views import CustomLoginView
from .views import CustomRegisterView
from django.contrib.auth.views import LogoutView
from .views import index

urlpatterns = [

    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("", index, name="home"),
]
