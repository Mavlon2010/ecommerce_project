from rest_framework.routers import DefaultRouter

from backend.apps.products.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet

routers = DefaultRouter()
routers.register('category', CategoryViewSet)
routers.register('subcategory', SubCategoryViewSet)
routers.register('product', ProductViewSet)

urlpatterns = []
urlpatterns += routers.urls