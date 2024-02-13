from django.urls import path
# from . import views
from .views import RoomView, CategoryView
# from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token

app_name = 'room'
# router= DefaultRouter()
# router.register('room/',views.RoomView)
# router.register('passangers',views.PassangerViewSet)
# router.register('reservations',views.ReservationViewSet)


urlpatterns = [
    # path("",views.rooms, name='rooms'),
    path('list/', RoomView.as_view({'get': 'list'}), name="room_list"),
    path('category-list/', CategoryView.as_view({'get': 'list'}), name="category_list"),
    # path('get_a_room_detail/<str:room_slug>/', RoomDetailView.as_view(), name="single_room"),
    # path("room/<slug:slug>", views.room_info, name='room_info'),
    # path("search/<slug:category_slug>", views.list_category, name='list_category'),
]
