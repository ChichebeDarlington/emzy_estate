from django.urls import path
from . import views

app_name = "user_estates" #tells the project the particular app this name urls belongs to.

# urls patterns for post app
urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]