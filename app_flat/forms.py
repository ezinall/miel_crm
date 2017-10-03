from django import forms

# Create your forms here.

from .models import FlatUsage


class FlatUsageForm(forms.ModelForm):
    class Meta:
        model = FlatUsage
        exclude = ['major', 'date_pub', 'date_change', 'name', 'active']
