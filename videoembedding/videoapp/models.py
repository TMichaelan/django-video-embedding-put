from embed_video.fields import EmbedVideoField
from django.db import models

class EmbeddedVideoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    video = EmbedVideoField()
    class Meta:
        ordering = ['title']