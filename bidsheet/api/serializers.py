from rest_framework import serializers
from bidsheet.models import BidSheet

from accounts.api.serializers import UserPublicSerializer

class BidSheetSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BidSheet
        fields = [
            'uri',
            'id',
            'user',
            'job_name',
            'bill_to',
            'email',
            'address',
            'city',
            'phone',
            'order_taken_by',
            'date_ordered',
            'date_promised',
            'description',
            'total_materials_and_labor',
            'extras',
            'total_for_extras',
            'grand_total'
        ]
        read_only_fields = [
            'user',
        ]

    def get_uri(self, obj):
        return "/api/bidsheet/{id}/".format(id=obj.id)

    def validate(self, data):
        content = data.get('job_name', None)
        email = data.get('email', None)
        if content == "" or email == "":
            raise serializers.ValidationError('Job Name and email are required')
        return data

class BidSheetInlineUserSerializer(BidSheetSerializer):
    class Meta:
        model = BidSheet
        fields = [
            'uri',
            'id',
            'job_name',
            'bill_to',
            'email',
            'address',
            'city',
            'phone',
            'order_taken_by',
            'date_ordered',
            'date_promised',
            'description',
            'total_materials_and_labor',
            'extras',
            'total_for_extras',
            'grand_total'
        ]
