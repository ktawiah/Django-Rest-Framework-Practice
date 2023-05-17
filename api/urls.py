from django.urls import path, include
from rest_framework import routers
from api.views import BookModelViewSet, ProgressViewset, CategoryViewset

router = routers.DefaultRouter()
router.register("books", BookModelViewSet)
router.register("categories", CategoryViewset)
router.register("progress", ProgressViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
]
