from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    # Use the users.User model to validate and serialize API data.
    class Meta:
        model = User
        # Return the requested identity, contact, and image fields.
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile_number",
            "profile_picture",
        )
        # The database creates the ID, so clients cannot change it.
        read_only_fields = ("id",)