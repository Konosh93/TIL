from posts.models import Post,Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(slug_field='username',read_only=True)
	class Meta:
		model = Post
		fields = ('id','title','author','text','date_created','tags','likes')

class CommentSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(slug_field='username',read_only=True)
	class Meta:
		model = Comment
		fields = ('id','author','post','text','date_created','likes')

