from rest_framework import viewsets, exceptions, mixins
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Group, Post


class CommentPostBaseMixin(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):

    def perform_create(self, serializer):
        if self.serializer_class == CommentSerializer:
            serializer.save(author=self.request.user, post=self.get_post())
        else:
            serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                f"Вы не можете редактировать чужие {self.object_viewset}!")
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                f"Вы не можете удалять чужие {self.object_viewset}!")
        super().perform_destroy(instance)


class CommentViewSet(CommentPostBaseMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    object_viewset = 'комментарии'

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        return self.get_post().comments


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(CommentPostBaseMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    object_viewset = 'посты'
