from django.db import models
from accounts.models import User

# Create your models here.
class Event(models.Model):
    
    EVENT_STATUS = (
        ('Active', 'Active'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed')
    )
    
    EVENT_TYPE = (
    ('Church', 'Church'),
    ('School', 'School'),
    ('Sports', 'Sports'),
    ('Concert', 'Concert'),
    ('Conference', 'Conference'),
    ('Art', 'Art'),
    ('Theater', 'Theater'),
    ('Festival', 'Festival'),
    ('Workshop', 'Workshop'),
    ('Party', 'Party'),
    ('Charity', 'Charity'),
    ('Wedding', 'Wedding'),
    ('Gaming', 'Gaming'),
    ('Fashion', 'Fashion'),
    ('Food', 'Food'),
    ('Technology', 'Technology'),
    ('Business', 'Business'),
    ('Health', 'Health'),
    ('Music', 'Music'),
    ('Other', 'Other'),
)
    
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    date_and_time = models.DateTimeField()
    venue = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=EVENT_STATUS)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.event_name