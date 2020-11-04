
from django.urls import path
from InstituteApplication import views

urlpatterns = [
    path('',views.Home_View,name='home'),
    path('home',views.Home_View,name='home'),
    path('contact',views.Contact_View,name='contact'),
    path('service',views.Service_View,name='service'),
    path('feedback',views.Feedback_View,name='feedback'),
    path('login',views.Login_View,name='login'),
    path('gallery',views.Gallery_View,name='gallery')
]

