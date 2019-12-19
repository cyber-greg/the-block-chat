from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import Channel
from django.core import serializers


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def channels(request):

    if request.method == 'GET':
       channelID = request.GET.get('id', None)
       chatroomID = request.GET.get('chatroom', None)
    #    channelID = channel
       print("GET CHANNEL FROM ID >>> {}".format(channelID))
       print("GET CHATROOM FROM CHANNEL >>> {}".format(chatroomID))

    elif request.method == 'POST':
        pass
        # data = json.loads(request.body)
        # print("CONTENT >>> {}".format(data['content']))
        # channelID = data['channel']
        # new_message = Message(
        #     content=data['content'],
        #     date=data['date'],
        #     author=data['author'],
        #     channel=data['channel'] # ! get channel from channelID
        # )
        # new_message.save()

    response = []
    if channelID:
        response = Channel.objects.filter(id=channelID)

    if chatroomID:
        response = Channel.objects.filter(chatroom__id__contains=chatroomID)

    # data = serializers.serialize('json', response)
    # return HttpResponse(data, content_type="application/json")

    parsed_response = []

    for channel in response:

        allowedUserIds = []
        for user in channel.allowed_users.all():
            allowedUserIds.append(str(user.id))

        parsed_response.append({
            "id": str(channel.pk),
            "chatroomId": str(channel.chatroom.id),
            "userIds": allowedUserIds,
            "name": channel.name,
            "isPrivate": channel.private

        })

    print("PARSED_RESPONCE > {}".format(parsed_response))

    return JsonResponse(parsed_response, safe=False)
