from django.db import models

class demp(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accept'
    REJECTED = 'reject'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]
    employee_name = models.CharField(max_length=100)
    employee_code = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)  # Assuming maximum length of mobile number is 15 characters
    upload = models.FileField(upload_to='uploads/')
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
