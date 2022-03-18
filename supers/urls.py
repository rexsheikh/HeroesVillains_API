from django.urls import path
from . import views

urlpatterns = [
    path('',views.super_list),
    path('<int:pk>/',views.super_detail),
    path('<int:pk>/<int:id>/',views.power_patch)
]