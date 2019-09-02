from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('web_recovery.urls')),
    path('', include('api_recovery.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('users/', include('users.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
