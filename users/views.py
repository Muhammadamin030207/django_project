from rest_framework import status
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializers,LoginSerializer,MeSerializer,ProfileUpdateSerializer

class RegisterView(CreateAPIView):
    serializer_class=RegisterSerializers

class UserListView(ListAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()



class LoginView(CreateAPIView):
    serializer_class=LoginSerializer

    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data['user']
        refresh=RefreshToken.for_user(user)
        
        return Response(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=status.HTTP_200_OK
        )

class MeView(RetrieveAPIView):
    serializer_class=MeSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user

class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class=ProfileUpdateSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.user


    
class MyProfileView(RetrieveAPIView):
    serializer_class=MeSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)