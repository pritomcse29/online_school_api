from django.contrib import admin
from django.urls import path,include
from .views import CourseViewSet
urlpatterns = [
    path('',CourseViewSet.as_view(), name = "course-view" ),
]