from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()


class RegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self,attrs):
        user=authenticate(
            username=attrs['username'],
            password=attrs['password']
        )
        if not user:
            raise serializers.ValidationError('Username yoki password xato')
        
        attrs['user']=user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        if attrs.get("role") == "super_admin":
            if User.objects.filter(role="super_admin").exists():
                raise serializers.ValidationError(
                    "Projectda faqat bitta super_admin bo'lishi mumkin."
                )
        return attrs


class UserRoleChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['role']
        
