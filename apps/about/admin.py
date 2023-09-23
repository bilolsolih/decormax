from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Email, Address, PhoneNumber, SocialMedia, CompanyStat, CompanyHistory

admin.site.register(Address, TranslationAdmin)
admin.site.register(Email)
admin.site.register(PhoneNumber)
admin.site.register(SocialMedia)
admin.site.register(CompanyStat)
admin.site.register(CompanyHistory)
