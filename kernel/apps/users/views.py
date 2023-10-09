from django.http import Http404
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .emails import send_activation_mail
from .permissions import IsOwnerOrReadOnly

from .models import MyUser
from .serializers import ChangePasswordSerializer, RestorePasswordCompleteSerializer, RestorePasswordSerializer, \
    UserSerializer, LoginSerializer, MyUserDetailSerializer
from ..admin_panel.models import Clients
from ..admin_panel.serializers import ClientsSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegistrationView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = MyUser.objects.create_user(
                username=request.data['username'],
                nickname=request.data['nickname'],
                user_surname=request.data['user_surname'],
                email=request.data['email'],
                phone_number=request.data['phone_number'],
                password=request.data['password'],
            )
            user.save()
            user.generate_mixed_text()
            # send_activation_mail(serializer.data['email'], user.create_activation_code())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        my_user = self.get_object(pk)
        transactions = Clients.objects.filter(user_id=pk)

        transactions_serializer = ClientsSerializer(transactions, many=True)
        serializer = MyUserDetailSerializer(my_user)
        data = {
            'detail': serializer.data,
            'transactions': transactions_serializer.data,
        }
        return Response(data)


class ActivationView(APIView):
    def get(self, request, otp):
        try:
            user = MyUser.objects.get(otp=otp)
            user.is_active = True
            user.otp = ''
            user.save()
            return Response('Вы успешно активировали аккаунт')
        except MyUser.DoesNotExist:
            raise Http404


class RestorePasswordView(APIView):
    serializer_class = RestorePasswordSerializer

    def post(self, request):
        data = request.data
        serializer = RestorePasswordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_code()
            return Response('Вам выслан код верификации')


class RestorePasswordCompleteView(APIView):
    serializer_class = RestorePasswordCompleteSerializer

    def post(self, request):
        data = request.data
        serializer = RestorePasswordCompleteSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлён')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = ChangePasswordSerializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлён')
