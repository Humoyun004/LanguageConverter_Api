from django.urls import path

from . import views

urlpatterns = [
    path('api/convert_text/', views.TextView.as_view(), name='convert_text'),
    path('api/convert_file/', views.FileView.as_view(), name='convert_file'),
]