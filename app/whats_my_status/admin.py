from django.contrib import admin
from .models import AmountSpent, TimeSpent

# Register your models here.
admin.site.register(AmountSpent)
admin.site.register(TimeSpent)