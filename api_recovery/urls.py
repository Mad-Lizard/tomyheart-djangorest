from django.urls import path, include
from api_recovery import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/posts', views.PostViewSet)
router.register(r'api/users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
