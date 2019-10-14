from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sentences', views.SentenceView)

urlpatterns = [
    path('', include(router.urls)),
]