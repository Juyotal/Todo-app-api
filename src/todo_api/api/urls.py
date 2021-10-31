from . import views
from django.urls import path
from django.urls.conf import include

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name = 'api_view'),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-Update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-Delete"),
]