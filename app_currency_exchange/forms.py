from django import forms

from .current_convert_api import get_currency_json


class CurrencyExchangeFrom(forms.Form):
    
    currency_list = get_currency_json()

    from_currency = forms.ChoiceField(
        choices=currency_list, 
        widget=forms.Select(attrs={'class' : 'form-select'}), 
        label='From Currency'
        )
    to_currency = forms.ChoiceField(
        choices=currency_list, 
        widget=forms.Select(attrs={'class' : 'form-select',}), 
        label='To Currency'
        )
    currency_ammount = forms.IntegerField(
        min_value=1, 
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Currency Ammount'}), 
        label=''
        )