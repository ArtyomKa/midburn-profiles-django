# Generated by Django 2.1.4 on 2019-09-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190905_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burnevent',
            name='etc',
        ),
        migrations.AddField(
            model_name='burnevent',
            name='details',
            field=models.TextField(default='Default'),
            preserve_default=False,
        ),
    ]