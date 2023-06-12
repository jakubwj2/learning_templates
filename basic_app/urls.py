from django.urls import path
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path("other", views.other, name="other"),
    path("relative", views.relative, name="relative"),
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
]
