from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Purchase,Course
from courses.serializers import CourseSerializer
from .serializers import PurchaseSerializer
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CourseEnrollmentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get My Enrolled Courses",
        operation_description="Returns a list of courses the authenticated user is enrolled in.",
        responses={200: CourseSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def my_courses(self, request):
        student = request.user  
        purchases = Purchase.objects.filter(student=student).select_related('course')
        courses = [purchase.course for purchase in purchases]  
        serializer = CourseSerializer(courses, many=True, context={'request': request})
        return Response(serializer.data)  

    @swagger_auto_schema(
        operation_summary="Enroll in a Course",
        operation_description="Enroll the authenticated user in a course using the course name.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['course_name'],
            properties={
                'course_name': openapi.Schema(type=openapi.TYPE_STRING, description='The name of the course to enroll in'),
            },
        ),
        responses={
            201: PurchaseSerializer(),
            400: 'Already enrolled or invalid input',
            404: 'Course not found',
            500: 'Server error'
        }
    )
    @action(detail=False, methods=['post'])
    def enroll(self, request):  
        course_name = request.data.get('course_name')

        if not course_name:
            return Response({"detail": "Course name is required"}, status=400)

        try:
            course = Course.objects.get(name=course_name)
        except Course.DoesNotExist:
            return Response({"detail": "Course not found"}, status=404)

        student = request.user

        if Purchase.objects.filter(student=student, course=course).exists():
            return Response({"detail": "You are already enrolled in this course"}, status=400)

        try:
            with transaction.atomic():
                purchase = Purchase.objects.create(
                    student=student,
                    course=course,
                    amount=course.price
                )
                purchase_serializer = PurchaseSerializer(purchase)
            return Response(purchase_serializer.data, status=201)

        except Exception as e:
            return Response({"detail": str(e)}, status=500)



# class CourseEnrollmentViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]

#     @action(detail=False, methods=['get'])
#     def my_courses(self, request):
#         student = request.user  
#         purchases = Purchase.objects.filter(student=student).select_related('course')
#         courses = [purchase.course for purchase in purchases]  
#         serializer = CourseSerializer(courses, many=True, context={'request': request})
#         return Response(serializer.data)  
    
#     @action(detail=True, methods=['post'])
#     def enroll(self, request, pk=None): 
#         student = request.user
#         try:
#             course = Course.objects.get(pk=pk)  
#         except Course.DoesNotExist:
#             return Response({"detail": "Course not found"}, status=404)
    
#         if Purchase.objects.filter(student=student, course=course).exists():
#             return Response({"detail": "You are already enrolled in this course"}, status=400)
        
#         try:
          
#             with transaction.atomic():
#                 purchase = Purchase.objects.create(student=student, course=course, amount=course.price)
#                 purchase_serializer = PurchaseSerializer(purchase)
            
#             return Response(purchase_serializer.data, status=201)
        
#         except Exception as e:
#             return Response({"detail": str(e)}, status=500)
