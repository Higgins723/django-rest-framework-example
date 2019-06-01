from django import forms
from .models import BidSheet

class BidSheetForm(forms.ModelForm):
    class Meta:
        model = BidSheet
        fields = [
            'user',
            'job_name',
            'bill_to',
            'address',
            'city',
            'phone',
            'order_taken_by',
            'date_ordered',
            'date_promised',
            'description',
            'total_materials_and_labor',
            'extras',
            'total_for_extras',
            'grand_total'
        ]
    
    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        job_name = data.get('job_name', None)
        if job_name == "":
            job_name = None

        if job_name is None:
            raise forms.ValidationError('Job name is required')
        return super().clean(*args, **kwargs)