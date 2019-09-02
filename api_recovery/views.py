from recovery.models import Post, Article, Athlet
from .serializers import PostSerializer, ArticleSerializer, AthletSerializer, UserSerializer
from recovery.permissions import IsCreatedByReadOnly
from django.utils import timezone
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'post/<int:pk>/': reverse('post-detail', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsCreatedByReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_published=True)
    serializer_class = ArticleSerializer

class AthletViewSet(viewsets.ModelViewSet):
    queryset = Athlet.objects.filter(published_at__lte=timezone.now())
    serializer_class = AthletSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
