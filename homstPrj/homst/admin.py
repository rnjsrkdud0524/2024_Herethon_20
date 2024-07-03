from django.contrib import admin
from .models import SafetyFilter, Accommodation,  SearchRecord

# Register your models here.

@admin.register(SafetyFilter)
class SafetyFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'review_score', 'price')
    search_fields = ('name', 'location')
    list_filter = ('safety_filters',)
    filter_horizontal = ('safety_filters',)

@admin.register(SearchRecord)
class SearchRecordAdmin(admin.ModelAdmin):
    list_display = ('destination', 'travel_date', 'travel_date2', 'people')
    search_fields = ('destination',)
    list_filter = ('travel_date', 'people', 'safety_filter')
    filter_horizontal = ('safety_filter',)