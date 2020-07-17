from rest_framework import serializers

from sites.models import UserRequest, BlockedSites


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['id', 'domain_name', 'description', 'user_email',
                  'created']

    def create(self, validated_data):
        validated_data['ip_address'] = self.context.get('request').META.get(
            "REMOTE_ADDR")
        validated_data['additional_info'] = self.context.get('request').META.get(
            "HTTP_USER_AGENT")
        return UserRequest.objects.create(**validated_data)


class UserRequestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['domain_name', 'description', 'user_email', 'ip_address',
                  'additional_info', 'created']


class BlockedSitesSerializer(serializers.ModelSerializer):
    site = UserRequestInfoSerializer(many=False, read_only=True)
    site_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BlockedSites
        fields = ['id', 'is_blocked', 'site', 'site_id', 'email_was_sent']



