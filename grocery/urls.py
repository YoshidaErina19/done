from django.urls import path
from . import views


app_name = 'grocery'
urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.GroceryListView.as_view(),name='grocery_list'),
    ]