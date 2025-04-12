from rest_framework import serializers
from .models import Course, Department
from decimal import Decimal

class CourseSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')  

    class Meta:
        model = Course
        fields = [
            'name', 'description', 'available_seat', 'department',
            'created_at', 'updated_at', 'instructor', 'price',
            'duration_in_hours', 'is_active', 'thumbnail', 'level',
            'price_with_tax'
        ]  

    def calculate_tax(self, course: Course):
        print(course.price)
        return round(course.price * Decimal(1.1), 2) 
            

class DepartmentSerializer(serializers.ModelSerializer):
     class Meta:
          model =  Department
          fields =['name','description']
