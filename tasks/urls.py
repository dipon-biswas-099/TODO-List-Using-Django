from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.HomeView, name="home"),
    path('task-create/', views.TaskCreate, name="task_create"),
    path('task-update/<pk>', views.TaskUpdate, name = 'task_update')
    
]
