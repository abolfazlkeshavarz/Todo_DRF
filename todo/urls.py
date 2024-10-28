from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', viewset=views.TodoViewsets)

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.detailed_view),
    path('cbv/', views.ListAPIView.as_view()),
    path('cbv/<int:todo_id>', views.DetailedListAPIView.as_view()),
    path('mixins/', views.MixinViews.as_view()),
    path('mixins/<int:pk>', views.MixinDetailedView.as_view()),
    path('generics/', views.TodoGenericAPIViews.as_view()),
    path('generics/<int:pk>', views.TodoGenericDetailedAPIView.as_view()),
    path('viewsets/', include(router.urls)),
    path('users/', views.UsersGenericAPI.as_view()),

]
