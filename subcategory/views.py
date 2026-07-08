from rest_framework import viewsets
from .models import  SubCategory
from .serializers import SubCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.select_related('category').all()
    serializer_class = SubCategorySerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["name"]