from django.urls import path
from . import views


app_name = 'grocery'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.GroceryListView.as_view(), name='grocery_list'),
    # path('grocery_create/', views.GroceryCreateView.as_view(), name='grocery_create'),
    path('grocery_create/', views.grocery_create, name='grocery_create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('grocery_delete/<int:pk>/', views.GroceryDeleteView.as_view(), name='grocery_delete'),
    ]