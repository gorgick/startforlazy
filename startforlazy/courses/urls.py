from django.urls import path
from .views import BaseView, CourseView, OrderView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('course/<str:slug>/', CourseView.as_view(), name='course'),
    path('course/<str:slug>/order/', OrderView.as_view(), name='order')
]