from django.contrib.auth import get_user_model, login
from django.core.mail import send_mail
from rest_framework import mixins, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.users.api.serializers.auth import LoginSerializer, SignUpSerializer
from apps.users.api.serializers.validation import AccountActivationSerializer
from apps.users.models import ActivationCode


class Login(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            if user is not None and user.email_comfirmed:
                login(request, user)
                response_data = {
                    "user_id": user.id,
                    "success": "Login successful",
                }
                response = Response(response_data, status=status.HTTP_200_OK)
                response["Authorization"] = f"Token {token.key}"
                return response
            elif user is not None and not user.email_comfirmed:
                return Response(
                    {"error": "Email not confirmed, please activate your account"}, status=status.HTTP_401_UNAUTHORIZED
                )
            else:
                return Response({"error": "Invalid Email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountActivation(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = AccountActivationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            activation_code = serializer.validated_data["code"]
            email_confirmed = ActivationCode.objects.filter(activation_code=activation_code).first()
            if email_confirmed:
                if email_confirmed.verify_activation_code(activation_code):
                    return Response({"success": "Account Activated"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid activation code"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Invalid activation code"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUp(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            # check if email already exists
            user = get_user_model().objects.filter(email=email).first()
            if user:
                return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            Token.objects.create(user=user)
            activation_code = ActivationCode(user=user)
            activation_code.create_activation_code()
            # Send Email
            subject = "Account Activation"
            message = f"Your activation code is {activation_code.activation_code}"
            from_email = "<my email>"
            to_email = [email]
            try:
                send_mail(subject, message, from_email, to_email, fail_silently=True)
            except Exception:
                return Response({"error": "Error sending email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(
                {"success": "Account created, check your email for activation code"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
