from django.contrib import admin
from django.urls import path, include
# from room import views
# from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', include('room.urls'))
]
