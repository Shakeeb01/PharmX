from django.contrib import admin
from .models import Medicine


class MedicineAdmin(admin.ModelAdmin):
    list_display= ['product_image','name','description','manufacture_date','expiry_date','price']
    
    
admin.site.register(Medicine,MedicineAdmin)