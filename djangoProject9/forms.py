from django import forms

from portfolio.models import Query


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['username', 'title']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control'}),
        }
