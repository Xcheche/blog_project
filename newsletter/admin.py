from django.contrib import admin
from .models import Newsletter
# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('email',)
    ordering = ('-date_added',)
    date_hierarchy = 'date_added'