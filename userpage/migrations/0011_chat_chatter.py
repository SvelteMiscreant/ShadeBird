# Generated by Django 3.1.1 on 2020-09-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0010_auto_20200920_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chatter',
            field=models.CharField(default='', max_length=900),
            preserve_default=False,
        ),
    ]
