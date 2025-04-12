from enrollment.models import Purchase
from django.db.models import Count, Sum
from datetime import timedelta
from django.utils import timezone
from calendar import monthrange
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

class AdminDashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]  

    @action(detail=False, methods=['get'])
    def statistics(self, request):
       
        last_week = timezone.now() - timedelta(weeks=1)
        last_month = timezone.now() - timedelta(weeks=4)

        
        courses_last_week = Purchase.objects.filter(purchase_date__gte=last_week).count()
        courses_last_month = Purchase.objects.filter(purchase_date__gte=last_month).count()

        most_purchased_courses = Purchase.objects.values('course').annotate(total=Count('course')).order_by('-total')[:5]
        top_students = Purchase.objects.values('student').annotate(total=Count('student')).order_by('-total')[:5]

        current_month = timezone.now().month
        if current_month == 1:
            previous_month = 12
            year = timezone.now().year - 1
        else:
            previous_month = current_month - 1
            year = timezone.now().year

        total_sales_current_month = Purchase.objects.filter(purchase_date__month=current_month).aggregate(Sum('amount'))
        total_sales_previous_month = Purchase.objects.filter(
            purchase_date__month=previous_month,
            purchase_date__year=year
        ).aggregate(Sum('amount'))

        data = {
            'courses_last_week': courses_last_week,
            'courses_last_month': courses_last_month,
            'most_purchased_courses': most_purchased_courses,
            'top_students': top_students,
            'total_sales_current_month': total_sales_current_month['amount__sum'] or 0,
            'total_sales_previous_month': total_sales_previous_month['amount__sum'] or 0,
        }

        return Response(data)
