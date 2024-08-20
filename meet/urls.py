from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create_meet/', views.CreateRoomView.as_view()),
    path('request_join/', views.RequestJoinRoomView.as_view()),
    path('update_membership/<str:room_name>/<int:user_id>', views.UpdateStatusView.as_view()),
    path('enter_room/<str:room_name>', views.EnterRoomView.as_view()),
    path('pending_list/<str:room_name>', views.PendingListView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
