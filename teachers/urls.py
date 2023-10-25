from django.urls import path

from teachers import views

urlpatterns = [
    path("",views.Home, name="Home"),
    path("about",views.about, name="About")
]
