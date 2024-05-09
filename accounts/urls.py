from django.urls import path
from .views import user_login, user_logout

urlpatterns = [
    path("user_login/", user_login, name = "user_login"),
    path("user_logout/", user_logout, name="user_logout")
]
