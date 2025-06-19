from django.urls import path
from . import views
urlpatterns =[
    path('',views.task_list,name='list'),
    path('create/',views.create_task,name='create')
]