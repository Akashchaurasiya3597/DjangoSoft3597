from InstituteApplication.models import FeedbackDatabase,CoursesDatabase,ContactDatabase
from .serializer import FeedbackSerializer,CoursesSerializer,ContactSerializer
from rest_framework.viewsets import ModelViewSet


class FeedbackViewSet(ModelViewSet):
    queryset = FeedbackDatabase.objects.all()
    serializer_class = FeedbackSerializer


class CoursesViewSet(ModelViewSet):
    queryset = CoursesDatabase.objects.all()
    serializer_class = CoursesSerializer


class ContactViewSet(ModelViewSet):
    queryset = ContactDatabase.objects.all()
    serializer_class = ContactSerializer