from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.list_items),
    path('insert/', views.insert_items, name = 'insert_item'),
    path('delete/<int:todo_id>', views.delete_item, name ='delete_item'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name ='logout')
]