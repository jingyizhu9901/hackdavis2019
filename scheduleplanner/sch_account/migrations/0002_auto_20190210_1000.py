# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-10 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='User ID')),
                ('cid', models.CharField(max_length=10, verbose_name='Class ID')),
                ('rel', models.CharField(max_length=10, verbose_name='Relationship')),
            ],
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='major',
            field=models.CharField(default='', max_length=100, verbose_name='Major'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='year',
            field=models.IntegerField(default=1, verbose_name='Year'),
        ),
    ]