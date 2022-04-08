from django.urls import path
from django.conf.urls import  include
from rest_framework import routers
from .views import CreateUserView

router = routers.SimpleRouter()

urlpatterns = [
    path('api/v1/register/', CreateUserView.as_view()),
    path('', include(router.urls)),
]

