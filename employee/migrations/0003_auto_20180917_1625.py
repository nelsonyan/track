# Generated by Django 2.0.5 on 2018-09-17 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20180906_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_access', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='employeelist',
            options={'ordering': ['phone_ex']},
        ),
        migrations.AddField(
            model_name='employeelist',
            name='remote_access',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.RemoteAccess'),
        ),
    ]