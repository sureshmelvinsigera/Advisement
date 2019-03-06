from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from apps.CSI.models import student


class StudentAdvisementForm(ModelForm):
    class Meta:
        model = student
        fields = [
            'std_id', 'firstname', 'lastname', 'major', 'email', 'phone', 'gpa', 'advisor'
        ]
        labels = {
            'std_id': 'Student ID',
            'firstname': 'First name',
            'lastname': 'Last name',
            'major': 'Major',
            'email': 'EMail',
            'phone': 'Phone',
            'gpa': 'Current GPA',
            'advisor': 'Advisor name'
        }

    widgets = {
        'firstname': forms.TextInput(attrs={'class': 'form-control'}),
        # 'publisher': forms.TextInput(attrs={'class': 'form-control'}),
        # 'author': forms.TextInput(attrs={'class': 'form-control'}),
        # 'price': forms.TextInput(attrs={'class': 'form-control'}),
        # 'pages': forms.TextInput(attrs={'class': 'form-control'}),
    }

    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     Row(
        #         Column('email', css_class='xxxx'),
        #     )
        # )
