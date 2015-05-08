from rest_framework import serializers

from campaigns.models import Campaign

"""
These aren't actually used i this app; only here 
as demontration of how the `ModelSerializer` works.
"""
class CampaignSerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField()
    slug = serializers.CharField()
    ended_at = serializers.DateTimeField()
    owner = serializers.Field(source='user.username')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.slug = attrs.get('slug', instance.slug)
            instance.ended_at = attrs.get('ended_at', instance.ended_at)
            return instance

        # Create new instance
        return Campaign(**attrs)