from django.urls import path
from.import views
from user.views import(
    registration_view,
)

app_name = "user"

urlpatterns = [
    path('',views.home, name='home'),
    path('register', registration_view, name="register")
]
