# Generated by Django 2.0 on 2017-07-31 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuits', '0004_tuitlocation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuitlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]