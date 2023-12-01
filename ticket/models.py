from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='engineer', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(null=True)
    date_assigned = models.DateTimeField(null=True)
    is_assigned = models.BooleanField(default=False)
    status = models.CharField(
        max_length=15, 
        choices=(
            ('Pending', 'Pending'),
            ('Active', 'Active'),
            ('Closed', 'Closed')
        )
    )
    is_resolved = models.BooleanField(default=False)
    resolution_steps = models.TextField(null=True)

    def __str__(self):
        return self.title



    
