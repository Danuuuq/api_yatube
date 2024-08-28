from rest_framework import serializers

from posts.models import Comment, Group, Post


<<<<<<< HEAD
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
=======
class BaseSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
>>>>>>> 42bc4d873d1a5b26748d4cbe3645be66d990d06c


class CommentSerializer(BaseSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


<<<<<<< HEAD
class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

=======
class PostSerializer(BaseSerializer):
>>>>>>> 42bc4d873d1a5b26748d4cbe3645be66d990d06c
    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image',
                  'group', 'pub_date')
