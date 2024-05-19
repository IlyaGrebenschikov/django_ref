from django.urls import path

from . import views


urlpatterns = [
    path('create_link/', views.create_referral_view, name='create_link'),
]
