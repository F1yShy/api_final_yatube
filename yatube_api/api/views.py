from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthAndSafeOrIsAuthorOfObjectPermission
from api.serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer,
)
from posts.models import Comment, Group, Follow, Post


class PostViewSet(viewsets.ModelViewSet):
    """
    Вьюсет с операциями GET, POST, PUT, PATCH, DELETE,
    реализующий получение списка постов, созданием новых постов,
    получением, редактированием и удалением постов по id.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthAndSafeOrIsAuthorOfObjectPermission]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет с операцией GET, реализующий получение списка групп и
    получением информации группы по id.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет с операциями GET, POST, PUT, PATCH, DELETE,
    реализующий получение списка комментариев определенного поста,
    созданием новых комментариев к определенному посту, получением,
    редактированием и удалением комментариев по id у определенного поста.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthAndSafeOrIsAuthorOfObjectPermission]

    def create_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))

    def get_queryset(self):
        return self.create_post().comments

    def perform_create(self, serializer):
        post = self.create_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    """
    Вьюсет с операциями GET и POST, реализующий получение списка подпищиков и
    добавляющий другого пользователя, которого нет в подписках, в список
    подписок.
    """

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        follower = serializer.validated_data["following"]
        followers_in_list = self.queryset.filter(
            user=self.request.user, following=follower
        )
        if followers_in_list.exists():
            raise ValidationError(
                "Ошибка! Вы уже подписаны на данного пользователя!"
            )
        if follower == self.request.user:
            raise ValidationError("Ошибка! Вы не можете подписаться на себя!")

        serializer.save(user=self.request.user)
