from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Department
from courses.serializers import CourseSerializer,DepartmentSerializer
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdminOrReadOnly,IsOwnerOrAdmin,IsStudentOrAdmin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from courses.filters import DepartmentFilter
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing courses:
    - Admins can create, update, delete
    - Instructors can see their own courses
    - Students and public can view course list/details
    - Filter by department
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']
    
    def get_permissions(self):
   
     if self.action in ['list', 'retrieve']:
        return [AllowAny()]


     if self.action in ['create', 'update', 'partial_update', 'destroy']:
        return [IsAuthenticated(), IsOwnerOrAdmin()]


     return [IsAuthenticated()]
    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Course.objects.all() 
        elif hasattr(user, 'is_instructor') and user.is_instructor:
            return Course.objects.filter(instructor=user) 
        else:
            return Course.objects.all()  
    def get_serializer_context(self):
      return {'request': self.request}



    
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsOwnerOrAdmin]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all departments",
        responses={200: DepartmentSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a single department by ID",
        responses={200: DepartmentSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new department",
        request_body=DepartmentSerializer,
        responses={201: DepartmentSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

