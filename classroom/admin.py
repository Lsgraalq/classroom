from django.contrib import admin
from .models import BoardMessage, Subject
# Register your models here.

class BoardMessageAdmin(admin.ModelAdmin):
    list_display = ('subject','title', 'content', 'deadline','published')
    list_display_links = ('subject','title','content', 'deadline')
    search_fields = ('title','content','subject', 'deadline')


admin.site.register(Subject)
admin.site.register(BoardMessage, BoardMessageAdmin)
