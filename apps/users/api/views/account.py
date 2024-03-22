from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.api.serializers.profile import ProfileChangeSerializer, ProfileSerializer


class Account(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = ProfileChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        for key, value in serializer.validated_data.items():
            setattr(user, key, value)
        user.save()
        return Response(ProfileSerializer(user).data)

    def retrieve(self, request, *args, **kwargs):
        return Response(ProfileSerializer(self.get_object()).data)
