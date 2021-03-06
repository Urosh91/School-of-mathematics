# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='new_videou_url',
            field=models.URLField(default='s'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
