# Generated by Django 3.1.4 on 2021-01-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flavors', '0002_auto_20210105_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
