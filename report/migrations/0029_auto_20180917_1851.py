# Generated by Django 2.0.5 on 2018-09-17 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0028_auto_20180917_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackheader',
            name='mockup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Mockup'),
        ),
    ]