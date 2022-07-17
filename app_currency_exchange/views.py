from django.shortcuts import render

from .forms import CurrencyExchangeFrom


# Create your views here.
def currency_exchange(request):
    form = CurrencyExchangeFrom
    if request.method == 'GET':
        return render(request, 'index.html', {'form': form})
    try:
        ammount = round(
        float(request.POST['to_currency']) * float(request.POST['currency_ammount']) / float(request.POST['from_currency']), 
        2
    )
    except ValueError:
        return render(request, 'index.html', {'form': form, 'message': 'Please enter a number'})

    return render(
        request, 'index.html', {
            'form': form, 
            'message': f"= {ammount}",
            }
    )