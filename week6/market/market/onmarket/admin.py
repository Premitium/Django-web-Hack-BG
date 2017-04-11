from django.contrib import admin


from .models import MarketCategory, MarketOffer

@admin.register(MarketCategory)
class MarketCategory(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(MarketOffer)
class MarketOffer(admin.ModelAdmin):
    list_display = ('item_name', 'price', 'category', 'author', 'created_at', 'content', 'image')
    search_fields = ('category', )
