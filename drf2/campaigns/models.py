from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User', related_name='campaigns', default=None, null=True)

    class Meta:
        pass