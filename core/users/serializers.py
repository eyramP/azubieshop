from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='profile.gender')
    phone_number = PhoneNumberField(source='profile.phone_number')
    profile_photo = serializers.ReadOnlyField(source='profile.profile_photo.url')
    country = CountryField(source='profile.country')
    city = serializers.CharField(source='profile.city')

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name',
            'last_name', 'gender', 'phone_number',
            'profile_photo', 'country', 'city',
        ]

    def to_representation(self, obj):
        representation = super(UserSerializer, self).to_representation(obj)
        if obj.is_superuser:
            representation['admin'] = True
        return representation


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('first_name', ''),
            'password1': self.validated_data.get('password1', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self)
        user.save()

        setup_user_email(request, user, [])
        user.email = self.cleaned_data.get('email')
        user.passowrd = self.cleaned_data.get('password1')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        return user


class RegisterAdminUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        email = attrs.get('email')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": 'A user with this email already exists.'})
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        if len(password) < 6:
            raise serializers.ValidationError({"password": "Password must be at least 6 charactera."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_staff'] = True
        validated_data['is_superuser'] = True

        return self.Meta.model.objects.create(**validated_data)


class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        email = attrs.get('email')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": 'A user with this email already exists.'})
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        if len(password) < 6:
            raise serializers.ValidationError({"password": "Password must be at least 6 charactera."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])

        return self.Meta.model.objects.create(**validated_data)


class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
