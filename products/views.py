from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminUser
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

    def get_permissions(self):
        if self.request.method == 'GET':
            return[AllowAny()]
        return[IsAuthenticated(),IsAdminUser()]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)