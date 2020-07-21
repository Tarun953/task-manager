from django.urls import path
from . import views

urlpatterns = [
    path('taskm', views.homeView, name='home'),
    path('add',views.addTodo, name='add'),
    path('completed/<todo_id>',views.completeTodo,name = 'complete'),
    path('incomplete/<todo_id>',views.incompleteTodo, name = 'incomplete'),
    path('delete/<todo_id>',views.deleteTodo, name = 'delete'),
    path('deleteall',views.deleteall, name='deleteall'),
    path('',views.loginPage, name='login'),
    path('register',views.registerPage, name='register'),
    path('logout',views.logoutUser, name = 'logout')
]