from django.contrib import admin
from .models import BidSheet
from .forms import BidSheetForm

# Register your models here.
class BidSheetAdmin(admin.ModelAdmin):
    list_display = ['job_name', 'address']
    form = BidSheetForm

admin.site.register(BidSheet, BidSheetAdmin)