from django.db import models
from events.models import Event

# Create your models here.
class Ticket(models.Model):
    TICKET_TYPE = (
        ('General Admission', 'General Admission'),
        ('VIP', 'VIP'),
        ('Student', 'Student'),
        ('Senior Citizen', 'Senior Citizen'),
        ('Child', 'Child'),
        ('Senior', 'Senior')
    )
    SALES_STATUS = (
        ('Available', 'Available'),
        ('Sold Out', 'Sold Out')
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=100, choices=TICKET_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    sales_start_date = models.DateTimeField()
    sales_end_date = models.DateTimeField()
    sales_status = models.CharField(max_length=20, choices=SALES_STATUS)  # Available, Sold Out
    
    def __str__(self):
        return self.ticket_type