
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from api.views import Todoapi

router = DefaultRouter()
router.register(r'Todo/', views.Todoapi , basename='todo')

urlpatterns = [
  path('', include(router.urls))
]
