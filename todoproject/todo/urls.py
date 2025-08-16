from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns =[
path('list/', views.task_list, name='list'),
path('', views.create_task, name='create'),
path('complete/<int:task_id>',views.complete,name='complete'),
path('delete/<int:task_id>/', views.delete_task, name='delete'),
path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
path('register/', views.register, name='register'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]