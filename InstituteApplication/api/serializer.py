from rest_framework.serializers import ModelSerializer
from InstituteApplication.models import ContactDatabase, CoursesDatabase, FeedbackDatabase


class ContactSerializer(ModelSerializer):
    class Meta:
        model = ContactDatabase
        fields = '__all__'


class CoursesSerializer(ModelSerializer):
    class Meta:
        model = CoursesDatabase
        fields = '__all__'


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedbackDatabase
        fields = '__all__'
