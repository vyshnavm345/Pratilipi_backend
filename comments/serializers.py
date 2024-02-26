from rest_framework import serializers
from users.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'article', 'date']
        # read_only_fields = ['user', 'date']
