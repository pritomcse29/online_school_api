from django.urls import path,include
from .views import DepartmentViewSet
urlpatterns = [
    path('',DepartmentViewSet.as_view(), name = "Department-view" ),
]