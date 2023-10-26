from django.urls import path
from . import views

app_name = "countdown"
urlpatterns = [
    path("", views.index, name="index"),
    path("onetime/<int:one_time_id>", views.one_time_detail, name="onetime"),
    path("repeatable/<int:repeatable_id>", views.repeatable_detail, name="repeatable"),
]
