from django import forms

class StockForm(forms.Form):
    stock_symbol = forms.CharField(label='', max_length=15,
        widget=forms.TextInput
        (attrs=
        {
        'list': 'symbols',
        'v-model': 'userInput',
        '@input': 'queryTheSymbol',
        'id': 'sym-input',
        'placeholder': 'Stock or ETF Symbol'
        
        }))