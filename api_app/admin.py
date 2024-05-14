from django.contrib import admin
from api_app.models import Book
# Register your models here.

class AdminMode(admin.ModelAdmin):
    list_display = ('name', 'store_name','fave')
    search_fields = ('name', 'store_name')


admin.site.register(Book,AdminMode)
