# Generated by Django 2.0.5 on 2018-09-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelist',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='employeelist',
            name='phone_ex',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]