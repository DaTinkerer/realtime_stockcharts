from django.shortcuts import render, redirect
import requests
from .forms import StockForm
from django.core.files import File
from .tasks import get_time_series_data

def search (request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        

        sym = form.cleaned_data['stock_symbol']
        request.session['sym'] = sym
        s = request.session
        print(s.session_key)
        print(request.session['sym'])
        print(request.user)

       
        return redirect('/info/')
    context = {
        'form':form,
        
    }
    return render(request, 'stock_info/search.html', context)

def info (request):
    sym = request.session['sym']
    get_time_series_data.delay(sym)

   
    return render(request, 'stock_info/info.html')



    