from django import forms
from .models import Surveyor

class SurveyorForm(forms.ModelForm):
    class Meta:
        model = Surveyor
        fields = "__all__"
        widgets = {
            'STDE' : forms.NumberInput(attrs= {'class':'form-control'}),
            'MTDE' : forms.NumberInput(attrs= {'class':'form-control'}),
            'SUDEM' : forms.NumberInput(attrs= {'class':'form-control'}),
            'SUDEC' : forms.NumberInput(attrs= {'class':'form-control'}),
            'MVDEH' : forms.NumberInput(attrs= {'class':'form-control'}),
            'MVDEV' : forms.NumberInput(attrs= {'class':'form-control'}),
            'MVDEA' : forms.NumberInput(attrs= {'class':'form-control'}),
            'SVDEH' : forms.NumberInput(attrs= {'class':'form-control'}),
            'SVDEV' : forms.NumberInput(attrs= {'class':'form-control'}),
            'FD' : forms.NumberInput(attrs= {'class':'form-control'}),
        }

    