from django.db import models
from django.conf import settings

class BidSheetQuerySet(models.QuerySet):
    pass

class BidSheetManager(models.Manager):
    def get_queryset(self):
        return BidSheetQuerySet(self.model, using=self._db)

# Create your models here.
class BidSheet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=150, null=True, blank=True)
    bill_to = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=150, null=True, blank=True)
    order_taken_by = models.CharField(max_length=150, null=True, blank=True)
    date_ordered = models.CharField(max_length=150, null=True, blank=True)
    date_promised = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    total_materials_and_labor = models.CharField(max_length=150, null=True, blank=True)
    extras = models.TextField(null=True, blank=True)
    total_for_extras = models.CharField(max_length=150, null=True, blank=True)
    grand_total = models.CharField(max_length=150, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BidSheetManager()

    def __str__(self):
        return str(self.job_name)[:50]

    class Meta:
        verbose_name = 'Bid Sheet'
        verbose_name_plural = 'Bid Sheets'

    @property
    def owner(self):
        return self.user