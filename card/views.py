from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Card
from .serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user).select_related('product')

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        existing_card = Card.objects.filter(user=self.request.user, product=product).first()
        if existing_card:
            existing_card.quantity += serializer.validated_data.get('quantity', 1)
            existing_card.save()
            self._instance = existing_card
        else:
            self._instance = serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(CardSerializer(self._instance).data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['delete'], url_path='clear')
    def clear(self, request, *args, **kwargs):
        Card.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
