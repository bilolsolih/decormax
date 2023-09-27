from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Picture, News


def delete_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.delete()
    return None


delete_selected.short_description = 'Delete selected objects'


class PictureInline(admin.TabularInline):
    model = Picture
    fields = ['photo']


class NewsAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'photo', 'is_header']
    # list_editable = ['is_header']
    list_filter = ['is_header']
    search_fields = ['title']
    actions = [delete_selected]
    inlines = [PictureInline]


class PictureAdmin(admin.ModelAdmin):
    actions = [delete_selected]


admin.site.register(Picture, PictureAdmin)
admin.site.register(News, NewsAdmin)

# Register your models here.
