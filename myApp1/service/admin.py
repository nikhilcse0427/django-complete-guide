from django.contrib import admin   # ✅ correct import
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_icon", "service_title","service_des")  # ✅ must match your model fields

admin.site.register(Service, ServiceAdmin)
