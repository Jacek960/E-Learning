from django.urls import path
from .views import SignUpView, UserProfile, UserUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user-profile/', UserProfile.as_view(), name='user_profile'),
    path('user-update/', UserUpdate.as_view(), name='user_update'),
]
