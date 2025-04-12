
from django.urls import path
from .views import CourseEnrollmentViewSet

urlpatterns = [
    path('enrollments/<int:pk>/enroll/', CourseEnrollmentViewSet.as_view({'post': 'enroll'}), name='course-enroll'),
    path('my-courses/', CourseEnrollmentViewSet.as_view({'get': 'my_courses'}), name='my-courses'),
]
