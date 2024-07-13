from django.urls import path
from . import views
urlpatterns = [
    path('', views.view_home),
    path('json/', views.todo_json),
    path('jsons/', views.todo_jsons),

]
