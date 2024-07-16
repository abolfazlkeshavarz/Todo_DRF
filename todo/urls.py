from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.detailed_view),
    path('cbv/', views.ListAPIView.as_view()),
    path('cbv/<int:todo_id>', views.DetailedListAPIView.as_view()),

]
