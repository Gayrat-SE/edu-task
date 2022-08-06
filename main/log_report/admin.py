from django.contrib import admin

# Register your models here.
from log_report.models import Log




class AdminPanel(admin.ModelAdmin):
    list_display = ('upload_log', 'username', 'method', 'request', 'status')
    search_fields = ('username', 'upload_log')
    list_filter = ('status',)

admin.site.register(Log, AdminPanel)