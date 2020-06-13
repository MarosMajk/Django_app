from django import forms
from .models import FormView

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255,label="Meno")
    email = forms.EmailField(max_length=255,label="E-mail")
    ico = forms.CharField(max_length=8,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Zadajte IČO '}))


class ViewForm(forms.ModelForm):
    class Meta:
        model = FormView
        fields = ('name','email','ico')