from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth import get_user_model
User = get_user_model()
from ..models import Chatroom


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def chatrooms(request):

    if request.method == 'GET':
       chatroomID = request.GET.get('id', None)
       userID = request.GET.get('user', None)

       print("GET CHATROOM FROM ID >>> {}".format(chatroomID))

    elif request.method == 'POST':
        chatroomID = None
        data = json.loads(request.body.decode('utf-8'))

        # get JSON data
        name = data['name']
        userID = data['userId']

        user = User.objects.get(pk=userID)

        # create new channel
        new_chatroom = Chatroom(
            name=name
        )

        new_chatroom.save()
        new_chatroom.chatroom_admins.add(user)


    # ##################### #
    # get data for response #
    # ##################### #
    response = []

    if chatroomID:
        response = Chatroom.objects.filter(id=chatroomID)
    elif userID:
        response = Chatroom.objects.filter(chatroom_admins__in=userID)

    # ######################## #
    # format response for http #
    # ######################## #
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

    return JsonResponse(parsed_response, safe=False, json_dumps_params={'ensure_ascii': False})
