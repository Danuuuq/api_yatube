from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import path, include

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='comment')
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router_comment = routers.DefaultRouter()

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
