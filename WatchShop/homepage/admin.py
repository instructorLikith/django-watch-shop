from django.contrib import admin
from .models import Watches, WatchesUploads, Wishlist, Cart

# Register your models here.
admin.site.register(Watches)
admin.site.register(Wishlist)
admin.site.register(Cart)



class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description']

admin.site.register(WatchesUploads, WatchesUploadsAdmin)
