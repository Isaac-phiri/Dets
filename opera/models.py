from django.db import models
from accounts.models import User
from events.models import Event


# Create your models here.


class Order(models.Model):
    
    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    )
    
    PAYMENT_STATUS = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    order_date_and_time = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS)  # Pending, Confirmed, Cancelled
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)  # Paid, Unpaid
    additional_notes = models.CharField(max_length=200)
    
    def __str__(self):
        return self.order_status
    
class Promotion(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    promotion_code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_usage_per_user = models.IntegerField(default=1)  # Maximum times a user can use this promotion
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Minimum order amount to be eligible for the promotion
    usage_count = models.IntegerField(default=0)  # Number of times this promotion has been used
    active = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.promotion_code 
        
class Seat(models.Model):
    
    SEAT_TYPE = (
        ('Regular', 'Regular'),
        ('VIP', 'VIP')
    )
    
    AVAILABILITY_STATUS = (
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Sold', 'Sold')
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=20)
    seat_type = models.CharField(max_length=20)  # Regular, VIP
    availability_status = models.CharField(max_length=20)  # Available, Reserved, Sold
    
    def __str__(self):
        return self.seat_number


    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.notification_type
    
    

class RefundExchange(models.Model):
    
    REFUND_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_status = models.CharField(max_length=20)  # Pending, Completed
    reason = models.TextField()
    
    def __str__(self):
        return self.refund_amount[0:5]