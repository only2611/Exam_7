from django.contrib import admin

# Register your models here.
from interview.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id','question', 'created_at',]
    list_display_links = ['question']
    list_filter = ['question']
    search_fields = ['question', 'created_at',]
    fields = ['question', 'created_at',]
    readonly_fields = ['created_at',]
    # filter_horizontal = ['types']

admin.site.register(Poll, PollAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','variant', 'poll']
    list_display_links = ['variant']
    list_filter = ['variant']
    search_fields = ['variant']
    fields = ['variant', 'poll']

admin.site.register(Choice, ChoiceAdmin)