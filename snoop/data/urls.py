from django.urls import path
from . import views

urlpatterns = [
    path('<name>/json', views.collection),
    path('<name>/feed', views.feed),
]