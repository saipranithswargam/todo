from django.urls import path
from .views import RegisterView, LoginView, CreateTodoView, ListTodoView, UpdateTodoView, DeleteTodoView, FilterTodoByStatusView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('todos/create/', CreateTodoView.as_view(), name='create_todo'),
    path('todos/read/', ListTodoView.as_view(), name='list_todos'),
    path('todos/<int:pk>/update/', UpdateTodoView.as_view(), name='update_todo'),
    path('todos/<int:pk>/delete/', DeleteTodoView.as_view(), name='delete_todo'),
    path('todos/status/<str:status>/', FilterTodoByStatusView.as_view(), name='filter_todos_by_status'),
]
