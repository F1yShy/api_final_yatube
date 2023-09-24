from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="post")
v1_router.register("groups", GroupViewSet, basename="group")
v1_router.register(
    r"posts/(?P<post_id>[0-9]+)/comments",
    CommentViewSet,
    basename="comment",
)
v1_router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/", include("djoser.urls.jwt")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
