from rest_framework.routers import DefaultRouter
from .views import  SubCategoryViewSet


router = DefaultRouter()
router.register('', SubCategoryViewSet)

urlpatterns = router.urls
