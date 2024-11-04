from django.urls import path

from .views import ShowCheckOut, CheckOut

urlpatterns = [
    path("ShowCheckOut/", ShowCheckOut, name="ShowCheckOut"),
    path("CheckOut/", CheckOut, name="CheckOut"),

]
