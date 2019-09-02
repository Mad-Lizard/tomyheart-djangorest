from django.urls import path, include

urlpatterns = [
    path('', include('recovery.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
