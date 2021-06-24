from django import forms

class StockForm(forms.Form):
    stock_symbol = forms.CharField(label='', max_length=15,
        widget=forms.TextInput
        (attrs={'placeholder': 'Stock or ETF symbol'}))