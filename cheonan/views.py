from django.shortcuts import render
from django.contrib import messages
from .forms import CustomerForm
from django.db.models import Q
from .models import Customer
import re

def index(request):
    return render(request, 'cheonan/index.html')

def information(request):
    return render(request, 'cheonan/information.html')

def location(request):
    return render(request, 'cheonan/location.html')

def direction(request):
    return render(request, 'cheonan/direction.html')

def concierge(request):
    return render(request, 'cheonan/concierge.html')

def smart(request):
    return render(request, 'cheonan/smart.html')

def premium(request):
    return render(request, 'cheonan/premium.html')

def block(request):
    return render(request, 'cheonan/block.html')

def dong(request):
    return render(request, 'cheonan/dong.html')

def pyeong(request):
    return render(request, 'cheonan/pyeong.html')
    
def apply(request):
    success = False
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')

            # 전화번호 유효성 검사 (11자리 또는 13자리 숫자와 '-'만 허용)
            if not re.fullmatch(r'^\d{11}$|^\d{3}-\d{4}-\d{4}$', phone_number):
                messages.error(request, '전화번호는 11자리 또는 13자리 숫자와 "-"만 사용 가능합니다.')
            else:
                # 중복된 전화번호 확인
                if Customer.objects.filter(Q(phone_number=phone_number)).exists():
                    messages.error(request, '이미 등록된 전화번호입니다.')
                else:
                    form.save()
                    messages.success(request, '등록되었습니다.')
                    success = True
    else:
        form = CustomerForm()

    return render(request, 'cheonan/apply.html', {'form': form, 'success': success})