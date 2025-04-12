from enrollment.models import Purchase  
from rest_framework import serializers
from courses.models import Course

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['student', 'course', 'purchase_date', 'amount']


class CourseSerializer(serializers.ModelSerializer):
    is_enrolled = serializers.SerializerMethodField()  

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_enrolled(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Purchase.objects.filter(course=obj, student=request.user).exists()
        return False

