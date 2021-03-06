

from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import TrackHeader, PublicComment

class IssueInput(forms.ModelForm):
    class Meta:
        model = TrackHeader
        fields = '__all__'
        widgets = {
            'dead_line': DatePickerInput(options={"format": "MM-DD-YYYY"}),
            'date_requested': DatePickerInput(options={"format": "MM-DD-YYYY"}),
            'comments': forms.Textarea(attrs={'rows':32, 'cols':110}),

            'task_name': forms.TextInput(attrs={'size':110}),

            'sku_count': forms.TextInput(attrs={'size':55}),
            'google_url': forms.TextInput(attrs={'size':110}),
            'google_url_name': forms.TextInput(attrs={'size':110}),
            'marklyn_url': forms.TextInput(attrs={'size':110}),
            'marklyn_url_name': forms.TextInput(attrs={'size':110}),
        }

class PublicCommentForm(forms.ModelForm):
    class Meta:
        model = PublicComment
        fields = '__all__'
        widgets = {
            'public_comments': forms.Textarea(attrs={'rows':3, 'cols':120}),
            
        }
