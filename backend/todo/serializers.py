from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'title',
            'url',
            'completed',
            'order'
        )
