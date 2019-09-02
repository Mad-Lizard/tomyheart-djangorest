from django.urls import path, include

urlpatterns = [
    path('', include('api_recovery.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
