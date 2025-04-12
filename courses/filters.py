from django_filters.rest_framework import FilterSet,CharFilter
from .models import Department

class DepartmentFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Department
        fields = {
             'id': ['exact'],
            'name': ['exact', 'icontains'],
        }