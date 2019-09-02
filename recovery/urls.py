from django.urls import path
from recovery import views
from rest_framework.urlpatterns import format_suffix_patterns

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })
post_detail = views.PostViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retreive'
})

urlpatterns = [
    path('api', views.api_root),
    path('posts/', post_list, name='post-list'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('users/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
