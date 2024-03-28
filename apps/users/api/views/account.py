from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.api.serializers.profile import ProfileChangeSerializer, ProfileSerializer


class Account(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

    @action(detail=False, methods=["put", "patch"])
    def modify(self, request, *args, **kwargs):
        serializer = ProfileChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        for key, value in serializer.validated_data.items():
            setattr(user, key, value)
        user.save()
        return Response(ProfileSerializer(user).data)

    @action(detail=False, methods=["get"])
    def me(self, request):
        return Response(ProfileSerializer(request.user).data)

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == "modify":
            return ProfileChangeSerializer
        return ProfileSerializer
