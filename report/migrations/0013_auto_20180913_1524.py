# Generated by Django 2.0.5 on 2018-09-13 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0012_auto_20180907_1900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trackheader',
            options={'ordering': ['-report_key']},
        ),
    ]
