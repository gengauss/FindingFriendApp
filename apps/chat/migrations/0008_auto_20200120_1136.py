# Generated by Django 3.0 on 2020-01-20 02:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20200120_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='link',
            field=models.URLField(default=uuid.UUID('fa13c129-3aa8-46a6-aba9-7b7e52832a18')),
        ),
    ]
