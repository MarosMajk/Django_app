from django.urls import path
from . import views

urlpatterns = [
    path("",views.FormView_detail),
    path("form",views.index),
]

