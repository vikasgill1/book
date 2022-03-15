from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
TokenVerifyView
)

urlpatterns = [
    path('userReg/',UserRegister.as_view()),
    path('editUser/',UserProfile.as_view()),
    path('notes/',NoteView.as_view()),
    path('AdminUserReg/',AdminUserRegister.as_view()),
    path('AdminEditUser/',UserAdminEdit.as_view()),
    path('noteEdit/',NoteAdmin.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]