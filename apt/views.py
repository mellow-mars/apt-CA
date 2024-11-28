from django.shortcuts import render
from .forms import CustomerForm

def home(request):
    return render(request, 'index.html')

def information(request):
    return render(request, 'apt/information.html')

def location(request):
    return render(request, 'apt/location.html')

def direction(request):
    return render(request, 'apt/direction.html')

def concierge(request):
    return render(request, 'apt/concierge.html')

def smart(request):
    return render(request, 'apt/smart.html')

def premium(request):
    return render(request, 'apt/premium.html')

def block(request):
    return render(request, 'apt/block.html')

def dong(request):
    return render(request, 'apt/dong.html')

def pyeong(request):
    return render(request, 'apt/pyeong.html')
    
def apply(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')  # Redirect or render a success page
    else:
        form = CustomerForm()

    return render(request, 'apt/apply.html', {'form': form})