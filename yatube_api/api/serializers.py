from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для поста."""

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("post",)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для группы."""

    class Meta:
        fields = "__all__"
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписки."""

    user = SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = "__all__"
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=["user", "following"],
                message="Ошибка, вы уже подписаны на данного пользователя",
            )
        ]

    def validate_following(self, value):
        """Проверка, что пользователь не может подписаться сам на себя"""

        if self.context["request"].user == value:
            raise serializers.ValidationError(
                "Ошибка! Вы не можете подписаться на себя!"
            )
        return value
