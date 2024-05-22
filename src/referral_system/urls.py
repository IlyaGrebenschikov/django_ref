from django.urls import path

from . import views


urlpatterns = [
    path('create_link/', views.create_referral_view, name='create_link'),
    path('delete_link/', views.delete_referral_view, name='delete_link'),
    path('show_referrers/', views.show_referrers_view, name='show_referrers'),
    path('add_link/', views.add_referral_view, name='add_link'),
]
