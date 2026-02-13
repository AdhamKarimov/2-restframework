from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.UserListView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('update/<int:pk>', views.UserUpdateView.as_view()),
    path('detail/<int:pk>', views.UserDetailView.as_view()),
    path('delete/<int:pk>', views.UserDeleteView.as_view()),
]