from django.db import models

class WorkingSet(models.Model):
    identifier = models.TextField(default="")
    vidCategory = models.TextField(default="")
    vidTag = models.TextField(default="")
    vidURL = models.TextField(default="")

class RecordingSet(models.Model):
    identifier = models.TextField(default="")
    category = models.TextField(default="")
    tag = models.TextField(default="")
    url = models.TextField(default="")
    abort = models.TextField(default="")
    ended = models.TextField(default="")
    error = models.TextField(default="")
    pause = models.TextField(default="")
    play = models.TextField(default="")
    playing = models.TextField(default="")
    seeked = models.TextField(default="")
    seeking = models.TextField(default="")
    timeupdate = models.TextField(default="")
    volumechange = models.TextField(default="")
    waiting = models.TextField(default="")
    rating = models.TextField(default="")
    timestopped = models.TextField(default="")
    comment = models.TextField(default="")
    date = models.TextField(default="")
