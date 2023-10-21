from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'nickname', 'username', 'user_surname', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class MyUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email_or_phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = None
        if '@' in data['email_or_phone_number']:
            user = MyUser.objects.filter(email=data['email_or_phone_number']).first()
        else:
            user = MyUser.objects.filter(phone_number=data['email_or_phone_number']).first()

        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return {
                'id': user.id,
                'email': user.email,
                'phone_number': user.phone_number,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'is_admin': user.is_admin,
                'is_superuser': user.is_superuser,
                'check_code': user.check_code,
            }
        raise serializers.ValidationError('Incorrect email/phone number or password')


class RestorePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        if not MyUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с указанным email не зарегистрирован')
        return email

    def send_verification_code(self):
        email = self.validated_data.get('email')
        user = MyUser.objects.get(email=email)
        user.create_activation_code()
        send_mail(
            'Восстановление пароля',
            f'Ваш код верификации: {user.otp}',
            'test@gmail.com',
            [user.email]
        )


class RestorePasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=20, min_length=20)
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('otp')
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if not MyUser.objects.filter(email=email, otp=code).exists():
            raise serializers.ValidationError('Пользователь не найден')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')
        return super().validate(attrs)

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = MyUser.objects.get(email=email)
        user.set_password(password)
        user.save()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate_old_password(self, password):
        user = self.context['request'].user
        if not user.check_password(password):
            raise serializers.ValidationError('Неверный пароль')
        return password

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')
        return super().validate(attrs)

    def set_new_password(self):
        user = self.context['request'].user
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()
