from django import forms
from .models import Records

GENDER_CHOICES = (
    (None, '-------------------------------------------'),
    ('M','MALE'),
    ('F','FEMALE')
)
class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['name', 'age', 'gender', 'city', 'state', 'pincode', 'country', 'dol', 'last_seen', 'dob', 'mobileno','image', 'status']

        widgets = {
            'gender' : forms.Select(choices=GENDER_CHOICES)
        }