from django.shortcuts import render
from django.contrib import messages
from . forms import CustomerForm
from django.db.models import Q
from . models import Customer
import re

def index(request):
    return render(request, 'cheongju/index.html')

def information(request):
    return render(request, 'cheongju/information.html')

def location(request):
    return render(request, 'cheongju/location.html')

def direction(request):
    return render(request, 'cheongju/direction.html')

def of_premium(request):
    return render(request, 'cheongju/of_premium.html')

def of_block(request):
    return render(request, 'cheongju/of_block.html')

def of_dong(request):
    return render(request, 'cheongju/of_dong.html')

def of_commu(request):
    return render(request, 'cheongju/of_commu.html')

def apt_danzi(request):
    return render(request, 'cheongju/apt_danzi.html')

def apt_block(request):
    return render(request, 'cheongju/apt_block.html')

def apt_dong(request):
    return render(request, 'cheongju/apt_dong.html')

def apt_commu(request):
    return render(request, 'cheongju/apt_commu.html')

def apt_pyeong(request):
    return render(request, 'cheongju/apt_pyeong.html')

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

    return render(request, 'cheongju/apply.html', {'form': form, 'success': success})

def robots_txt(request):
    conetnt = """User-agent: *
Disallow: /admin/

Sitemap: https://kor-apt.info/sitemap-cheonan.xml
Sitemap: https://kor-apt.info/sitemap-yangju.xml
Sitemap: https://kor-apt.info/sitemap-cheongju.xml
"""
    return HttpResponse(content, content_type="text/plain")