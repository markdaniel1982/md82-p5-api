from django.urls import path
from tasks import views


urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('tasks/prioritychoices', views.PriorityChoicesViewSet.as_view()),
    path('tasks/statuschoices', views.StatusChoicesViewSet.as_view()),
    path('tasks/privacychoices', views.PrivacyChoicesViewSet.as_view()),
]
