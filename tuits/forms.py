from django import forms
from .models import TuitLocation
from .validators import validate_category

class TuitCreateForm(forms.Form):
    name            = forms.CharField()
    location        = forms.CharField(required=False)
    category        = forms.CharField(required=False)

    
class TuitLocationCreateForm(forms.ModelForm):
#    category = forms.CharField(required=False,validators=[validate_category])
#    email = forms.EmailField()
    class Meta:
        model=TuitLocation
        fields=[
                'name',
                'location',
                'category',
                'slug'
                ]
#        exclude=[]
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Nombre invalido')
        return name
    
#    def clean_email(self):
#        email=self.cleaned_data.get('email')
#        if 'edu' in email:
#            raise forms.ValidationError('No aceptamos emails .edu')
#        return email   
