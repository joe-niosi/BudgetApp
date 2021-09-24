from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index), #get, renders home.html
    path('create', views.add_expense),
    path('delete/<int:expense_id>', views.delete_expense),
    path('edit/<int:expense_id>', views.edit_expense),
    path('update/<int:expense_id>', views.update_expense),
]
