# Generated by Django 3.0 on 2020-01-20 02:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20200120_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='link',
            field=models.URLField(default=uuid.UUID('97a09625-4b2b-461a-b92a-094355806bc2')),
        ),
    ]
