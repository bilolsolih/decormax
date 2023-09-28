from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Email, Address, PhoneNumber, SocialMedia, CompanyStat, CompanyHistory, ContactPhoneNumber, Contact, \
    ShowroomDetails, Showroom


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    list_display_links = ['id']
    list_editable = ['email']
    search_fields = ['email']


@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ['id', 'region', 'district', 'street', 'house_no']
    list_display_links = ['id']
    list_editable = ['region', 'district', 'street', 'house_no']
    search_fields = ['region', 'district', 'street', 'house_no']


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number']
    list_display_links = ['id']
    list_editable = ['phone_number']
    search_fields = ['phone_number']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'social_media', 'link']
    list_display_links = ['id', 'social_media']
    list_editable = ['link']


@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ['id', 'icon', 'title']
    list_display_links = ['id']
    list_editable = ['icon', 'title']
    search_fields = ['title']


@admin.register(CompanyHistory)
class CompanyHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'content']
    list_display_links = ['id', 'year', 'content']


@admin.register(ContactPhoneNumber)
class ContactPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    ordering = ['id']
    list_per_page = 10


class ShowroomDetailAdmin(admin.TabularInline):
    model = ShowroomDetails


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'video']
    list_per_page = 10
    list_display_links = ['id', 'title', 'video']
    ordering = ['id']
    inlines = [ShowroomDetailAdmin]
