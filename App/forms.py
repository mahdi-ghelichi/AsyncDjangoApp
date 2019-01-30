from django import forms


class JobForm(forms.Form):
    job_name = forms.CharField(label='Job name', required=True)
