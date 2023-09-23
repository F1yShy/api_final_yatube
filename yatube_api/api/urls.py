from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

ver1_router = DefaultRouter()
ver1_router.register("posts", PostViewSet, basename="post")
ver1_router.register("groups", GroupViewSet, basename="group")
ver1_router.register(
    r"posts/(?P<post_id>[0-9]+)/comments",
    CommentViewSet,
    basename="comment",
)

urlpatterns = [
    path("v1/", include(ver1_router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
    path(
        "v1/follow/", FollowViewSet.as_view({"get": "list", "post": "create"})
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
