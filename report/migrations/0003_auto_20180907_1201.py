# Generated by Django 2.0.5 on 2018-09-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20180907_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackheader',
            name='date_requested',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trackheader',
            name='dead_line',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
    ]