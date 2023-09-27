from django.contrib import admin

from .models import Inquiry, InquiryCall


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'email']

    def get_queryset(self, request):
        qs = self.model._default_manager.filter(is_call=False)
        ordering = self.get_ordering(request)
        if ordering:
            qs.order_by(*ordering)
        return qs


@admin.register(InquiryCall)
class InquiryCallAdmin(InquiryAdmin):
    def get_queryset(self, request):
        qs = self.model._default_manager.filter(is_call=True)
        ordering = self.get_ordering(request)
        if ordering:
            qs.order_by(*ordering)
        return qs
