from django.urls import path

from . import views

urlpatterns = [
    #path('api/v1/todos/', views.TodoList.as_view()),
    #path('api/v1/todos/<todo_id>/', views.TodoOne.as_view(), name='todo_one'),
    path('', views.TodoList.as_view()),
    path('<todo_id>/', views.TodoOne.as_view(), name='todo_one'),
]
