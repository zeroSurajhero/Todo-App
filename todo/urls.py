from django.urls import path


from . import views



urlpatterns = [
    path("", views.ToDoHome.as_view(), name="todo-home"),
    path("login/", views.LoginView.as_view(), name="log-in"),
    path("logout/", views.LogoutView.as_view(), name="log-out"),
    path("signup/", views.SignupView.as_view(), name="sign-up"),
    path("remove-todo/<int:pk>/", views.remove_todo, name="remove-todo"),
    path("change-status/<int:pk>/<str:status>", views.change_todo_status, name="change-status"),
]
