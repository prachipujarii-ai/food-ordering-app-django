from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),    #empty string because of the home page, usually.
    path('item/<int:pk>/',views.MenuItemDetail.as_view(), name="menu_item")
]




