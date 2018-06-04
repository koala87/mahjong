from django.db import models


MAX_LENGTH = 128


class Game(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, blank=False, null=False)
    circle = models.IntegerField(default=0, blank=False, null=False)
    base = models.IntegerField(default=0, blank=False, null=False, db_column='base')
    member1 = models.CharField(max_length=MAX_LENGTH, blank=False, null=False)
    member2 = models.CharField(max_length=MAX_LENGTH, blank=False, null=False)
    member3 = models.CharField(max_length=MAX_LENGTH, blank=False, null=False)
    member4 = models.CharField(max_length=MAX_LENGTH, blank=False, null=False)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    score3 = models.IntegerField(default=0)
    score4 = models.IntegerField(default=0)
    start_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Record"

    def __unicode__(self):
        return self.name


class Record(models.Model):
    round = models.IntegerField(default=0, blank=False, null=False)
    score1 = models.IntegerField(default=0, blank=False, null=False)
    score2 = models.IntegerField(default=0, blank=False, null=False)
    score3 = models.IntegerField(default=0, blank=False, null=False)
    score4 = models.IntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.round
