from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Purchase,Course
from courses.serializers import CourseSerializer
from .serializers import PurchaseSerializer
from django.db import transaction

class CourseEnrollmentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def my_courses(self, request):
        student = request.user  
        purchases = Purchase.objects.filter(student=student).select_related('course')
        courses = [purchase.course for purchase in purchases]  
        serializer = CourseSerializer(courses, many=True, context={'request': request})
        return Response(serializer.data)  
    
    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None): 
        student = request.user
        try:
            course = Course.objects.get(pk=pk)  
        except Course.DoesNotExist:
            return Response({"detail": "Course not found"}, status=404)
    
        if Purchase.objects.filter(student=student, course=course).exists():
            return Response({"detail": "You are already enrolled in this course"}, status=400)
        
        try:
          
            with transaction.atomic():
                purchase = Purchase.objects.create(student=student, course=course, amount=course.price)
                purchase_serializer = PurchaseSerializer(purchase)
            
            return Response(purchase_serializer.data, status=201)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=500)
