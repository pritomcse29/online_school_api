from django.urls import path
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet,DepartmentViewSet
from enrollment.views import CourseEnrollmentViewSet
from dashboards.views import AdminDashboardViewSet

# Create a router and register the CourseViewSet
router = DefaultRouter()
router.register(r'courses', CourseViewSet,basename='course')
router.register(r'departments',DepartmentViewSet)
router.register(r'enrollments', CourseEnrollmentViewSet, basename='course-enrollment')
router.register(r'admin/dashboard', AdminDashboardViewSet, basename='admin-dashboard')

urlpatterns = router.urls
