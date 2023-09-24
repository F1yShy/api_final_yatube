from rest_framework import mixins, viewsets


class GetPostViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    Кастомный базовый класс для вьюсета, возвращающий список объектов
    для метода GET и создающий объект методом POST
    """

    pass
