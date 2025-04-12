from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    

   
class Course(models.Model):
    levels =(
    ('beginner','Beginner'),
    ('intermediate','Intermediate'), 
    ('advanced','Advanced')
    )
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    available_seat = models.PositiveIntegerField()

    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='courses')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    duration_in_hours = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    thumbnail = CloudinaryField('image')
    # thumbnail = models.ImageField(upload_to="courses/images/")
    level = models.CharField(max_length=20,default='beginner',choices=levels)

    class Meta:
        ordering = ['-id',]
    def __str__(self):
        return self.name
    
# class ProductImage(models.Model):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(
#         upload_to="products/images/", validators=[validate_file_size])
# class ProductImage()
