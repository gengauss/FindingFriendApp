# Generated by Django 3.0 on 2020-01-20 02:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20200120_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='link',
            field=models.URLField(default=uuid.UUID('ba95830b-0b1a-42bd-8f5b-19b1e2fc0e14')),
        ),
    ]