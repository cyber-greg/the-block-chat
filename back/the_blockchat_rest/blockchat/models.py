from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.



class Chatroom(models.Model):
    """ A chatroom is a place that contains one or more channel """

#   id: string;
#   AdminIds: string[];
#   name: string;

    chatroom_admins = models.ManyToManyField(
        User,
        verbose_name="Administrateurs de la chatroom",
    )

    name = models.CharField(
        verbose_name="Nom Chatroom",
        max_length=100
    )

    def __str__(self):
        return "{}".format(
            self.name
        )

class Channel(models.Model):
    """ A channel is a place where a discussion takes place """

#   id: string;
#   chatroomId: string;
#   userIds: string[];
#   name: string;
#   isPrivate: boolean;

    name = models.CharField(
        verbose_name="Nom Channel",
        max_length=100
    )

    chatroom = models.ForeignKey(
        Chatroom,
        verbose_name="Chatroom",
        on_delete=models.CASCADE
    )

    allowed_users = models.ManyToManyField(
        User,
        verbose_name="Utilisateurs autorisés",
    )

    private = models.BooleanField(
        default=False,
        verbose_name="Conversation privée",
    )

    def __str__(self):
        return "{}".format(
            self.name
        )


class Message(models.Model):
    """A message posted by one user to one channel"""

#   id: string;
#   channelId: string;
#   userId: string;
#   content: string;
#   createdAt: string;

    channel = models.ForeignKey(
        Channel,
        verbose_name="Channel",
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        User,
        verbose_name="Author",
        on_delete=models.SET_NULL,
        null=True
    )

    content = models.TextField(
        verbose_name="Message",
    )

    created_at = models.DateTimeField(auto_now_add=True,
                                      blank=True,
                                      verbose_name="Created At")

    def __str__(self):
        return "{} : <{}> - {}".format(
            self.author,
            self.created_at,
            self.content
        )


