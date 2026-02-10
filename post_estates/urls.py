from django.urls import path
from . import views

app_name = "post_estates" #tells the project the particular app this name urls belongs to.

# urls patterns for post app
urlpatterns = [
    path("", views.fetch_post_view, name="home"),
    path("new_estate", views.create_post_view, name="new_estate"),
     path("<int:id>", views.estate_detail, name="details"),
     path("estate/<int:pk>/tab/<str:tab>/", views.estate_tab),

]