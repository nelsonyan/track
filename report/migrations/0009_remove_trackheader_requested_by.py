# Generated by Django 2.0.5 on 2018-09-07 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_auto_20180907_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackheader',
            name='requested_by',
        ),
    ]
