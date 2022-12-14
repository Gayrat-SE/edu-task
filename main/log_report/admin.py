from django.contrib import admin

# Register your models here.
from log_report.models import Log




class AdminPanel(admin.ModelAdmin):
    list_display = ('created_at', 'username', 'method', 'url', 'status')
    search_fields = ('username', 'created_at')
    list_filter = ('status',)

admin.site.register(Log, AdminPanel)