from django.shortcuts import render
from .models import Snippet
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class CreateSnippetRequest:

    def __init__(self, code, title=''):
        self.title = title
        self.code = code


class CreateSnippetRequestSerializer(serializers.Serializer):

    title = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100
    )
    code = serializers.CharField()

    def create(self, validated_data):
        snippet_data = CreateSnippetRequest(**validated_data)
        return snippet_data


class CreateSnippetResponseClass:

    def __init__(self, id, title, code):
        self.id = id
        self.title = title
        self.code = code


class CreateSnippetResponseSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100
    )
    code = serializers.CharField()

    def create(self, validated_data):
        return CreateSnippetResponseClass(**validated_data)


def create_snippet_in_db(title, code):

    from snippets.models import Snippet
    return Snippet.objects.create(title=title, code=code)


@api_view(['POST'])
def create_snippet(request):
    #print("request:",request)
    #print(request.data)

    serializer = CreateSnippetRequestSerializer(
    data=request.data    
    )

    is_valid_request_data = not serializer.is_valid()

    if is_valid_request_data:
        return Response(status=400)
    request_obj = serializer.save()
    '''print(
            "title: {}, code: {}".format(
                request_obj.title, request_obj.code
                )
            )'''
    '''dummy_snippet_object = CreateSnippetResponseClass(
            id=1,
            title=request_obj.title,
            code=request_obj.code
            )'''
    new_snippet_obj = create_snippet_in_db(
            request_obj.title, request_obj.code
            )
    response_serializer = CreateSnippetResponseSerializer(
            new_snippet_obj
        )
    return Response(response_serializer.data)


@api_view(['GET', 'POST'])
def get_list_of_snippets(request):
    if request.method == 'POST':
        print('hai prathap')
        return Response()

    print("hello", request.method)

    snippet_objs = Snippet.objects.all()
    response_serializer = CreateSnippetResponseSerializer(
            snippet_objs, many=True
    )
    return Response(response_serializer.data)



