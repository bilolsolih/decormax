from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Email, Address, PhoneNumber, SocialMedia, CompanyStat, CompanyHistory, Contact, ContactPhoneNumber


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    ordering = ['id']
    list_per_page = 10


admin.site.register(Address, TranslationAdmin)
admin.site.register(Email)
admin.site.register(PhoneNumber)
admin.site.register(SocialMedia)
admin.site.register(CompanyStat)
admin.site.register(CompanyHistory)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactPhoneNumber)
