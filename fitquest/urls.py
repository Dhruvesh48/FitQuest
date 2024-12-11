from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan_list, name='plan_list'),
    path('plans/<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('tasks/<int:plan_id>/', views.view_tasks, name='view_tasks'),
    path('tasks/update/<int:task_id>/', views.update_task_status, name='update_task_status'),
]