# Generated by Django 2.0 on 2017-07-31 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuits',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
