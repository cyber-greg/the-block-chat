from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

# import MODELS
from django.contrib.auth import get_user_model
User = get_user_model()
from ..models import Channel, Chatroom


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def channels(request):

    if request.method == 'GET':
        # get request parameters
        channelID = request.GET.get('id', None)
        chatroomID = request.GET.get('chatroom', None)
        userID = request.GET.get('user', None)

    elif request.method == 'POST':
        channelID = None
        userID = None
        data = json.loads(request.body.decode('utf-8'))

        # get JSON data
        name = data['name']
        chatroomID = data['chatroomID']
        allowed_userIDs = data['allowedUserIDs']
        private = data['private']

        # create new channel
        new_channel = Channel(
            name=name,
            chatroom=Chatroom.objects.get(pk=chatroomID),
            private=private
        )

        new_channel.save()
        new_channel.allowed_users.set(User.objects.filter(id__in=allowed_userIDs))


    # ##################### #
    # get data for response #
    # ##################### #
    response = []
    if channelID:
        response = Channel.objects.filter(id=channelID)

    elif chatroomID:
        response = Channel.objects.filter(chatroom__id__contains=chatroomID)

    elif userID:
        # get only channels with user in channel or admin of related chatroom
        user = User.objects.get(pk=userID)
        debug_response = Channel.objects.all()
        response = Channel.objects.filter(Q(allowed_users__in=[user]) | Q(chatroom__chatroom_admins__in=[user]))

    # ######################## #
    # format response for http #
    # ######################## #
    parsed_response = []

    for channel in response:

        allowedUserIds = []
        for user in channel.allowed_users.all():
            allowedUserIds.append(str(user.id))

        chatroomAdminIds = []
        for admin in channel.chatroom.chatroom_admins.all():
            chatroomAdminIds.append(str(admin.id))

        parsed_response.append({
            "id": str(channel.pk),
            "name": channel.name,
            "chatroomId": str(channel.chatroom.id),
            "chatroomName": str(channel.chatroom.name),
            "chatroomAdminIds": chatroomAdminIds,
            "userIds": allowedUserIds,
            "isPrivate": channel.private
        })

    return JsonResponse(parsed_response, safe=False, json_dumps_params={'ensure_ascii': False})
