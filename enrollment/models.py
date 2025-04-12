from django.db import models
from django.conf import settings  
from courses.models import Course
class Purchase(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    purchase_date = models.DateTimeField(auto_now_add=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    
    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.name}'
