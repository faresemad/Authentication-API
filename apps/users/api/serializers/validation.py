from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class AccountActivationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetVerifySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6)
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password], style={"input_type": "password"}
    )


class EmailChangeSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailChangeVerifySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6)
    new_email = serializers.EmailField()


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password], style={"input_type": "password"}
    )

    def validate(self, attrs):
        user = self.context["request"].user

        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError({"old_password": "Password is incorrect."})

        return attrs
