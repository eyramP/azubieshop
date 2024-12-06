from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import (
    UserLoginSerializer,
    UserSerializer,
    RegisterAdminUserSerializer,
    AdminLoginSerializer,
    RegisterUserSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema


User = get_user_model()


class CustomUserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()


class RegisterAdminUserView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
            request_body=RegisterAdminUserSerializer,
            responses={'201': UserSerializer}
    )
    def post(self, request, *args):
        data = request.data
        serializer = RegisterAdminUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': 'Admin account created successfully'}, status=status.HTTP_201_CREATED)


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
            request_body=RegisterUserSerializer,
            responses={'201': UserSerializer}
    )
    def post(self, request, *args):
        data = request.data
        serializer = RegisterUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': 'User account created successfully'}, status=status.HTTP_201_CREATED)


class AdminLoginView(APIView):
    permission_classes = [AllowAny]

    # / Swagger/Redoc documentation //////////
    @swagger_auto_schema(
        request_body=AdminLoginSerializer
        # responses={'200': serializers.ProductSerializer}
        )
    def post(self, request):
        serrializer = AdminLoginSerializer(data=request.data)
        if serrializer.is_valid():
            email = serrializer.validated_data['email']
            password = serrializer.validated_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

            if not user.is_staff and user.is_superuser:
                return Response({'error': 'Only admin users are allowed to use this login route'}, status=status.HTTP_403_FORBIDDEN)

            if not user.check_password(password):
                return Response({'error': 'Invalid credientials'}, status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })

        return Response(serrializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
            request_body=UserLoginSerializer
    )
    def post(self, request):
        serrializer = UserLoginSerializer(data=request.data)
        if serrializer.is_valid():
            email = serrializer.validated_data['email']
            password = serrializer.validated_data['password']
            password2 = serrializer.validated_data['confirm_password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

            if not password == password2:
                return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

            if not user.check_password(password):
                return Response({'error': 'Invalid credientials'}, status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })

        return Response(serrializer.errors, status=status.HTTP_400_BAD_REQUEST)
