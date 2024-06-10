from django.urls import path
from .views import Demo

urlpatterns = [
    path('', Demo.root_route, name='root'),
    path('login/', Demo.login_page, name='login'),
    path('register/', Demo.register_page, name='register')
]