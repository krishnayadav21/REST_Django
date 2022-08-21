from django.urls import path
from . import views

urlpatterns = [
    path('',views.read),
    path('create', views.create),
    path('update/<int:Emp_id>/', views.update),
    path('delete/<int:Emp_id>/', views.delete)
]