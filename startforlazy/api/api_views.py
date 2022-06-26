from rest_framework.generics import ListAPIView
from .serializers import CoursesSerializer
from courses.models import Course


class CoursesListApiView(ListAPIView):
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()
