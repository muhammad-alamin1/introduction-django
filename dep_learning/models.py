from django.db import models

# Create your models here.
class DeepLearning(models.Model):
    CATEGORY_CHOICES = [
        ('EL', 'Electronics'),
        ('CL', 'Clothing'),
        ('FD', 'Food'),
    ]
    
    _id = models.IntegerField
    algorithm = models.CharField(max_length=50)
    type = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    upload_file = models.FileField(upload_to='documents/')
    uploaded_image = models.ImageField(upload_to='images/')
    
    