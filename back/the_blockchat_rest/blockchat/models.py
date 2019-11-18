from django.db import models

# Create your models here.


class Message(models.Model):
    """An alert send to a specific user - the alert will be displayed in dashboard"""

    # "content": 'Premier message',
    # "date": '2019-11-16',
    # "author": 'greg@d82.io',
    # "channel": '1'

    content = models.TextField(
        verbose_name="Contenu",
    )

    date = models.TextField(
        verbose_name="Date",
    )

    author = models.TextField(
        verbose_name="Author",
    )

    channel = models.TextField(
        verbose_name="Channel",
    )

    created_at = models.DateTimeField(auto_now_add=True,
                                      blank=True,
                                      verbose_name="Create At")

    def __str__(self):
        return "{} : <{}> - {}".format(
            self.content,
            self.date,
            self.content
        )
