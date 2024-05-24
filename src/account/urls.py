from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('me/<int:pk>/', views.UserDetailView.as_view(), name='user-details'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
