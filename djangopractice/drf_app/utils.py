from datetime import datetime
from rest_framework import serializers


class Comment(object):

    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class User(object):
    def __init__(self, email, username):
        self.email = email
        self.username = username


class Profile(object):
    def __init__(self, profile):
        self.profile = profile


class ProfileSerializer(serializers.Serializer):
    profile = serializers.URLField(default='https://prathap.com/img')


class UserSerializer(serializers.Serializer):
    profile = ProfileSerializer()

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        profile = Profile(**profile_data)
        user = User(profile=profile, **validated_data)

        return user

    def update(self, instance,  validated_data):
        pass


class EditItem(object):
    def __init__(self, name):
        self.name = name


class EditItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    edits = EditItemSerializer(many=True)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
'''
    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
'''
