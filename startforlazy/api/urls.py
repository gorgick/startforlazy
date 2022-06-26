from django.urls import path
from .api_views import CoursesListApiView

urlpatterns = [
    path('courses/', CoursesListApiView.as_view())
]