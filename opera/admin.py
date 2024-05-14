from django.contrib import admin
from .models import Order, Promotion, Seat, Notification, RefundExchange

admin.site.register(Order)
admin.site.register(Promotion)
admin.site.register(Seat)
admin.site.register(Notification)
admin.site.register(RefundExchange)
