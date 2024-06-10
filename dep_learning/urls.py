from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.machine_learning, name='machine_learning'),
    path("deep-learning/", views.deep_learning, name='deep_learning')
]