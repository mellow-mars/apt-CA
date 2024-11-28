import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Customer

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = ('name', 'phone_number')  # 내보낼 필드 설정

    # 엑셀로 내보내는 함수
    def export_as_xlsx(self, queryset=None, *args, **kwargs):
        queryset = queryset or self.get_queryset()
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['이름', '전화번호'])  # 엑셀 첫 번째 행에 헤더 추가
        
        # 데이터를 엑셀 파일에 작성
        for obj in queryset:
            ws.append([obj.name, obj.phone_number, obj.enquiry])
        
        # 엑셀 파일을 반환
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'attachment; filename=customers.xlsx'
        wb.save(response)
        return response

class CustomerAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'phone_number')  # Admin에서 보여줄 필드
    resource_class = CustomerResource

    # 엑셀 내보내기 버튼을 추가
    actions = ['export_as_xlsx']

admin.site.register(Customer, CustomerAdmin)