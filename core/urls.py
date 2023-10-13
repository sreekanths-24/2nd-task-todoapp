from django.urls import path
from .views import SignupView, LoginView, TodoListCreateView, TodoDetailView

urlpatterns = [
    # Authentication endpoints
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

    # Todo endpoints
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]
