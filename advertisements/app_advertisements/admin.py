from django.contrib import admin
from .models import Advertisement
from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html
# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'price','created_date','updated_date','auction','image','user', 'get_thumbnail']
    list_filter = ['auction','created_at']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = (
        ("Общие", {
            'fields': ('title', 'description','image')
        }),
         ("Финансы", {
            'fields': ('price', 'auction'),
            'classes': ('collapse',),
        })
    )
    @admin.action(description="Убрать возможность торгов")
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)
        
    @admin.action(description="Вернуть возможность торгов")
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description='Изображение')
    def get_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            default_image_url = static('img/adv.png')
            return format_html('<img src="{}" width="50" height="50" />', default_image_url)

admin.site.register(Advertisement, AdvertisementAdmin)