from django.urls import path,include
from InstituteApplication import views
from .views import FeedbackViewSet,CoursesViewSet,ContactViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('feedback', FeedbackViewSet, basename='feedback'),
router.register('course', CoursesViewSet, basename='course'),
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('',include(router.urls)),

]