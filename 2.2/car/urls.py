from django.urls import path
from . import views


urlpatterns = [
    path('list', views.CarListAPIView.as_view()),
    path('create', views.CarCreateAPIView.as_view()),
    path('detail/<int:pk>', views.CarRetrieveAPIView.as_view()),
    path('update/<int:pk>', views.CarUpdateAPIView.as_view()),
    path('delete/<int:pk>', views.CarDestroyAPIView.as_view()),
]