# Generated by Django 3.0 on 2020-01-20 03:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20200120_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='link',
            field=models.URLField(default=uuid.UUID('fc4af166-86e2-4599-9031-7546e260c7c9')),
        ),
    ]
