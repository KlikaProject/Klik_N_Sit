from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.get_routes),

    # Authentication
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration
    path('register/', views.register_user, name='register new user'),

    # Tables
    path('table/', views.get_tables, name='get all tables'),
    path('table/<str:pk>/', views.get_table, name='get specific table'),

    # Address


    # for testing
    path('users/details/', views.get_user_details),

]
