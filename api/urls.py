from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sentences', views.SentenceViewSet)
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]