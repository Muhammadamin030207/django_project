from rest_framework import status
from rest_framework.generics import CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializers,LoginSerializer,UserSerializer,UserRoleChangeSerializer
from .permissions import IsAdminUser


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializers


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


class MeView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRoleChangeView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleChangeSerializer
    permission_classes = [IsAdminUser]