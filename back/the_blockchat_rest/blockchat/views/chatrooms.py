from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import Chatroom
from django.core import serializers


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def chatrooms(request):

    if request.method == 'GET':
       chatroomID = request.GET.get('id', None)
       userID = request.GET.get('user', None)

       print("GET CHATROOM FROM ID >>> {}".format(chatroomID))

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

    if chatroomID:
        response = Chatroom.objects.filter(id=chatroomID)
    # elif userID:
    #     response = Chatroom.objects.filter(chatroom__id__contains=channelID) # ! FIXME
    else:
        response = Chatroom.objects.all() # ! only chatroom where I am allowed

    # data = serializers.serialize('json', response)
    # return HttpResponse(data, content_type="application/json")

    parsed_response = []

    for chatroom in response:

        adminIds = []
        for admin in chatroom.chatroom_admins.all():
            adminIds.append(str(admin.id))

        parsed_response.append({
            "id": str(chatroom.pk),
            "name": chatroom.name,
            "adminIds": adminIds

        })

    print("PARSED_RESPONCE > {}".format(parsed_response))

    return JsonResponse(parsed_response, safe=False, json_dumps_params={'ensure_ascii': False})
