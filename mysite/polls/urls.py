from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("specifics/<int:question_id>/",     views.detail,    name="detail"),
    path(  "results/<int:question_id>/",     views.results,   name="results"),
    path(     "vote/<int:question_id>/",     views.vote,      name="vote"),
    path("randomstr/<str:valami>/",          views.randomstr, name="strval")
]

