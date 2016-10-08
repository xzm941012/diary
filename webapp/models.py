from django.db import models
import json

# Create your models here.
class JsonDumps():
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)

        return d

class Diary(models.Model):
    userid = models.IntegerField()
    contants = models.TextField()
    date = models.DateTimeField()
    imageurl = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        db_table = 'diary'


class User(models.Model,JsonDumps):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    relationid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'


class UserEncoder(json.JSONEncoder):
    def default(self, o):
        if(isinstance(o,User)):
            return[o.username,o.password,o.name,o.relationid]
        return json.JSONEncoder.default(self,o)

