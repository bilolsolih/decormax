from rest_framework import serializers

from apps.inquiries.models import Inquiry


class InquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['full_name', 'phone_number', 'on_collection', 'email']
