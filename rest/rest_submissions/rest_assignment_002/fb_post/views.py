from django.shortcuts import render
from .models import User, Post, Comment, Reaction
from .constants import ReactionEnum
from fb_post.utils.create_post import create_post as get_create_post
from fb_post.utils.get_post import get_post as get_post_details
from fb_post.utils.reply_to_comment import reply_to_comment as \
create_reply_to_comment
from fb_post.utils.react_to_post import react_to_post as \
create_react_to_post
from fb_post.utils.react_to_comment import react_to_comment as \
create_react_to_comment
from fb_post.utils.delete_post import delete_post as remove_post
from fb_post.utils.create_comment import create_comment as get_create_comment
from rest_framework import serializers
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from .exceptions import (
    InvalidUserException,
    InvalidPostContent,
    InvalidPostException,
    InvalidCommentException,
    InvalidReplyContent,
    InvalidReactionTypeException,
    UserCannotDeletePostException,
    InvalidCommentContent
)


class CreatePostRequest:
    def __init__(self, content):
        #self.user_id=user_id
        self.content=content

class CreatePostRequestSerializer(serializers.Serializer):
    #user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return CreatePostRequest(**validated_data)

class postidresponse:
    def __init__(self, post_id):
        self.post_id=post_id

class postidresponseSerialize(serializers.Serializer):
    post_id = serializers.IntegerField()
    def create(self, validated_data):
        return postidresponse(**validated_data)

class reactionSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    type = serializers.ListField(
        child=serializers.ChoiceField(
            choices=[react.value for react in ReactionEnum]
            )
        )

class userSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    profile_pic = serializers.URLField()

class repliescommentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = userSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField(max_length=1000)
    reactions= reactionSerializer()

class commentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = userSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField(max_length=1000)
    reactions= reactionSerializer()
    replies_count = serializers.IntegerField()
    replies = repliescommentSerializer(many=True)


class postSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    posted_by = userSerializer()
    posted_at = serializers.DateTimeField()
    post_content = serializers.CharField(max_length=1000)
    reactions= reactionSerializer()
    comments = commentSerializer(many=True)
    comments_count = serializers.IntegerField()

class createreplycommentrequest:
    def __init__(self, user_id, content):
        self.user_id=user_id
        self.content=content


class createreplycommentrequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)
    def create(self, validated_data):
        return createreplycommentrequest(**validated_data)

class commentidresponse:
    def __init__(self, comment_id):
        self.comment_id=comment_id

class commentidresponseSerialize(serializers.Serializer):
    comment_id = serializers.IntegerField()
    def create(self, validated_data):
        return commentidresponse(**validated_data)


class CreateReactToPostRequest:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type

class CreateReactToPostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.ChoiceField(
        choices=[
            react.value
            for react in ReactionEnum
            ]
        )
    def create(self, validated_data):
        return CreateReactToPostRequest(**validated_data)


class CreateReactToCommentRequest:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type

class CreateReactToCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.ChoiceField(
        choices=[
            react.value
            for react in ReactionEnum
            ]
        )
    def create(self, validated_data):
        return CreateReactToCommentRequest(**validated_data)

class CreateDeletePostRequest:
    def __init__(self, user_id):
        self.user_id=user_id

class CreateDeletePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    def create(self, validated_data):
        return CreateDeletePostRequest(**validated_data)

class CreateCommentRequest:
    def __init__(self, user_id, content):
        self.user_id=user_id
        self.content=content

class CreateCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return CreateCommentRequest(**validated_data)


@api_view(['POST'])
@authentication_classes([OAuth2Authentication])
@protected_resource(['superuser'])
def create_post(request):
    #print(request.__dict__)

    serializer = CreatePostRequestSerializer(data=request.data)
    is_not_valid = not serializer.is_valid()
    if is_not_valid:
        return Response(serializer.errors)

    data = serializer.save()

    try:
        post_id = get_create_post(
            request.resource_owner.id,
            data.content
        )

    except InvalidUserException:
        return Response(status=404)
    except InvalidPostContent:
        return Response(status=400)

    post_obj = postidresponse(post_id)
    post_dict = postidresponseSerialize(post_obj)
    return Response(post_dict.data, status=201)


@api_view(['GET'])
@authentication_classes([OAuth2Authentication])
@protected_resource(['superuser'])
def get_post(request, post_id):

    try:
        post_details = get_post_details(post_id)
    except InvalidPostException:
        return Response(status=404)

    postSerializer(post_details)
    return Response(post_details, status=200)


@api_view(['POST'])
def reply_to_comment(request, comment_id):

    comment_obj = createreplycommentrequestSerializer(data=request.data)
    is_not_valid = not comment_obj.is_valid()

    if is_not_valid:
        return Response(comment_obj.errors)

    data = comment_obj.save()

    try:
        comment_obj_id = create_reply_to_comment(
            data.user_id,
            comment_id,
            data.content
        )
    except InvalidUserException:
        return Response(status=404)
    except InvalidCommentException:
        return Response(status=404)
    except InvalidReplyContent:
        return Response(status=400)

    obj = commentidresponse(comment_obj_id)
    comment_dict = commentidresponseSerialize(obj)
    return Response(comment_dict.data, status=201)



@api_view(['POST'])
def react_to_post(request, post_id):

    serializer = CreateReactToPostRequestSerializer(data=request.data)

    is_not_valid = not serializer.is_valid()

    if is_not_valid:
        return Response(serializer.errors)

    data = serializer.save()

    try:
        create_react_to_post(
            data.user_id,
            post_id,
            data.reaction_type
        )

    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except InvalidReactionTypeException:
        return Response(status=400)
    return Response(status=200)


@api_view(['POST'])
def react_to_comment(request, comment_id):

    serializer = CreateReactToCommentRequestSerializer(data=request.data)

    is_not_valid = not serializer.is_valid()

    if is_not_valid:
        return Response(serializer.errors)

    data = serializer.save()

    try:
        create_react_to_comment(
            data.user_id,
            comment_id,
            data.reaction_type
        )

    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except InvalidReactionTypeException:
        return Response(status=400)
    return Response(status=200)

@api_view(['POST'])
def delete_post(request, post_id):

    serializer = CreateDeletePostRequestSerializer(data=request.data)
    is_not_valid = not serializer.is_valid()
    if is_not_valid:
        return Response(serializer.errors)

    data = serializer.save()

    try:
        remove_post(
            data.user_id,
            post_id
        )

    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except UserCannotDeletePostException:
        return Response(status=403)
    return Response(status=200)

@api_view(['POST'])
def create_comment(request, post_id):

    serializer = CreateCommentRequestSerializer(data=request.data)
    is_not_valid = not serializer.is_valid()
    if is_not_valid:
        return Response(serializer.errors)

    data = serializer.save()

    try:
        comment_id = get_create_comment(
            data.user_id,
            post_id,
            data.content
        )

    except InvalidUserException:
        return Response(status=404)
    except InvalidPostException:
        return Response(status=404)
    except InvalidCommentContent:
        return Response(status=400)

    comment_obj = commentidresponse(comment_id)
    comment_dict = commentidresponseSerialize(comment_obj)
    return Response(comment_dict.data, status=201)

