# Generated by Django 2.0.5 on 2018-09-14 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0020_auto_20180914_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_comments', models.TextField(blank=True, max_length=50000)),
            ],
        ),
        migrations.AlterField(
            model_name='trackheader',
            name='mockup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Mockup'),
        ),
    ]