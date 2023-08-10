from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models.product import Articul, Collection, Brand, Video
from .models.product_parameters import Color, Style, PictureType, TargetRoom, Size, ManufacturingMethod, BuildingMaterial
from .models.store import Store


def delete_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.delete()
    return None


delete_selected.short_description = 'Delete selected objects'


class VideoInline(admin.TabularInline):
    model = Video


class ArticulInCollection(admin.TabularInline):
    model = Articul


class CollectionAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'status', 'price', 'active']
    list_editable = ['status', 'active']
    inlines = [ArticulInCollection, VideoInline]


class ArticulAdmin(admin.ModelAdmin):
    actions = [delete_selected]

    def delete_model(self, request, obj):
        obj.delete()


class VideoAdmin(admin.ModelAdmin):
    actions = [delete_selected]


admin.site.register(Articul, ArticulAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Brand)
admin.site.register(Video, VideoAdmin)
admin.site.register(Store)
admin.site.register(Color)
admin.site.register(Style, TranslationAdmin)
admin.site.register(PictureType, TranslationAdmin)
admin.site.register(TargetRoom, TranslationAdmin)
admin.site.register(Size)
admin.site.register(ManufacturingMethod, TranslationAdmin)
admin.site.register(BuildingMaterial, TranslationAdmin)
