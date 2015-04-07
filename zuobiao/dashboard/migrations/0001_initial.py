# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField()),
                ('choice', models.IntegerField(verbose_name='答案', choices=[(1, '强烈反对'), (2, '反对'), (3, '同意'), (4, '强烈同意')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField()),
                ('sex', models.IntegerField(verbose_name='性别', choices=[(1, '男'), (2, '女')])),
                ('birthday', models.IntegerField(verbose_name='生日')),
                ('income', models.IntegerField(verbose_name='年收入', choices=[(1, '0-25k'), (2, '25k-50k'), (3, '50k-75k'), (4, '75k-100k'), (5, '100k-150k'), (6, '150k-300k'), (7, '300k+')])),
                ('education', models.IntegerField(verbose_name='学历', choices=[(1, '初中及以下'), (2, '高中'), (3, '大学'), (3, '研究生及以上')])),
                ('ip', models.CharField(max_length=32, verbose_name='IP')),
                ('country', models.CharField(blank=True, max_length=512, verbose_name='IP所在国', null=True)),
                ('province', models.CharField(blank=True, max_length=512, verbose_name='IP所在省', null=True)),
                ('city', models.CharField(blank=True, max_length=512, verbose_name='IP所在市', null=True)),
                ('operators', models.CharField(blank=True, max_length=512, verbose_name='IP所在运营商', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='anser',
            name='question',
            field=models.ForeignKey(to='dashboard.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='anser',
            name='user',
            field=models.ForeignKey(to='dashboard.User'),
            preserve_default=True,
        ),
    ]
