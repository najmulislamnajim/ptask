from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('addtask/',views.TaskFormView.as_view(),name='addtask'), 
    path('tasklist/',views.TaskListView.as_view(),name='tasklist'), 
    path('updatetask/<int:pk>',views.UpdateTaskListView.as_view(),name='updatetask'), 
    path('deletetask/<int:pk>',views.DeleteTaskView.as_view(),name='deletetask'), 
    path('deletecompletetask/<int:pk>',views.DeleteCompletedTaskView.as_view(),name='deletecompletetask'), 
    path('completedtask/',views.ComepletedTaskListView.as_view(),name='completedtask'), 
    path('completetask/<int:pk>',views.taskComeplete,name='completetask'), 
    path('about',views.About.as_view(),name='about'), 
]