from django.contrib import admin

from djangor.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'author', )
    list_display_links = ('pub_date', 'title', )
    ordering = ('-pub_date', )
    date_hierarchy = 'pub_date'
    exclude = ('pub_date', )


admin.site.register(Entry, EntryAdmin)
