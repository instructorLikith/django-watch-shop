from django.contrib import admin
from .models import Watches, WatchesUploads

# Register your models here.
admin.site.register(Watches)



class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchesUploads, WatchesUploadsAdmin)
