# Generated by Django 2.0.5 on 2018-09-14 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0021_auto_20180914_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackheader',
            name='mockup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Mockup'),
        ),
    ]
