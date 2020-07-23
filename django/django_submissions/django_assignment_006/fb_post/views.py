from django.shortcuts import render
from .models import User, Post, Comment, Reaction
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.



@api_view(['GET'])
def get_post_details(request):
    from django.utils.dateparse import parse_datetime

    import pytz
    from .utils import get_post

    post_detail = get_post(1)
    posted_time = parse_datetime(post_detail['posted_at'])
    print("1: post_posted_time ", posted_time, "**\n")

    amercia_mexico_time_zone = pytz.timezone('America/Mexico_City')
    print("america_time_zone: ",amercia_mexico_time_zone, "\n\n")
    india_kolkata_time_zone = pytz.timezone('Asia/Kolkata')
    print("india_time_zone: ",india_kolkata_time_zone, "\n\n")


    america_mexico_time = amercia_mexico_time_zone.localize(posted_time)
    print("america_mexico_time: ",america_mexico_time,"\n\n")
    india_kolkata_time = india_kolkata_time_zone.normalize(america_mexico_time.astimezone(india_kolkata_time_zone))
    print("india_kolkata_time: ", india_kolkata_time, "\n\n")
    india_kolkata_time_format = india_kolkata_time.strftime('%Y-%m-%d %H:%M:%s.%f')
    print("india_time_format: ", india_kolkata_time_format, "\n\n")
    post_detail['posted_at'] = india_kolkata_time_format
    print(post_detail)
    return Response(post_detail)
    #return HttpResponse(post_detail)

'''
def create_user_in_db(name, profile_pic):
    user_obj = User.objects.create(
        name=name,
        profile_pic=profile_pic
    )
    return user_obj
'''
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'profile_pic']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


@api_view(['POST'])
def user_posts(request):
    user_serializer = UserSerializer(data=request.data)

    if user_serializer.is_valid():
        user_obj = user_serializer.save()
        '''new_user_obj = create_user_in_db(
            name=user_obj.name,
            profile_pic=user_obj.profile_pic
            )'''
        user_dict = UserSerializer(user_obj)
        return Response(user_dict.data)
    return Response(user_serializer.errors)


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    users_dict = UserSerializer(users, many=True)
    return Response(users_dict.data)
