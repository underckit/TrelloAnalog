from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from boards import views

router = routers.DefaultRouter()
router.register(r'trellos', views.TrelloView, 'trello')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]