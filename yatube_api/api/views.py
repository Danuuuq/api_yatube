from rest_framework import viewsets, exceptions
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Comment, Group, Post


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Вы не можете редактировать чужие комментарии!")
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Вы не можете удалять чужие комментарии!")
        super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Вы не можете редактировать чужие записи!")
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Вы не можете удалять чужие записи!")
        super().perform_destroy(instance)
