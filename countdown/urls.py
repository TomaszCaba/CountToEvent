from django.urls import path
from . import views

app_name = "countdown"
urlpatterns = [
    path("", views.index, name="index"),
    path("onetime/<int:one_time_id>", views.one_time_detail, name="onetime"),
    path("repeatable/<int:repeatable_id>", views.repeatable_detail, name="repeatable"),
    path('profile/', views.profile, name='profile'),
    path('update/form/<str:counter_type>/<int:event_id>"', views.update_confirm, name='updateForm'),
    path('update/<str:counter_type>/<int:event_id>"', views.update_countdown, name='update'),
    path('create/form/', views.add_confirm, name='createForm'),
    path('delete/<str:counter_type>/<int:event_id>"', views.destroy_countdown, name='deleteForm'),
    path('create/', views.add_countdown, name='create'),
]
