# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-09 21:46
from __future__ import unicode_literals
import os,re
from django.db import migrations

def rating(apps,schema):
    Rating = apps.get_model("app","Rating")
    Movie = apps.get_model("app","Movie")
    User = apps.get_model("app","User")
    os.chdir("/home/avais/Desktop/recommend-movies/recommend-movies/app/")
    f = open("data/u.user", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('|', 5)
        if len(e) == 5:
            if e[4] > 0:
                User.objects.get_or_create(userid=e[0], age=e[1], sex=e[2], occupation=e[3], zipcode=e[4])
    f.close()
    f = open("data/u.item", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('|', 24)
        if len(e) == 24:
            Movie.objects.create(movieid=e[0], title=e[1], date=e[2], viddate=e[3], url=e[4], unknown=e[5], action=e[6], adventure=e[7], animation=e[8],
            childrens=e[9], comedy=e[10], crime=e[11], documentary=e[12], drama=e[13], fantasy=e[14], film_noir=e[15], 
            horror=e[16], musical=e[17], mystery=e[18], romance=e[19], sci_fi=e[20], thriller=e[21], \
            war=e[22], western=e[23])
    f.close()
    f = open("data/u.base", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('\t', 4)
        if len(e) == 4:
            Rating.objects.create(userid=e[0], movieid=e[1], rating=e[2], time=e[3])
    f.close()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160909_1830'),
    ]

    operations = [
        migrations.RunPython(rating),
    ]
