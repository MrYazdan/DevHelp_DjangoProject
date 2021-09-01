from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = []
        read_only_fields = ('is_accept',)
