from django.urls import path
from . import views

urlpatterns = [
    path('verbos/', views.verbos_list),
    path('verbos/<int:pk>/', views.verbos_detail),
]