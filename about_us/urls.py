from django.urls import path
from .views import Information

urlpatterns = [
    path("", Information.student_info),
]
