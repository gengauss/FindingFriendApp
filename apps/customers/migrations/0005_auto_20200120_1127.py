# Generated by Django 3.0 on 2020-01-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20200120_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='favorite_book',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='hobby',
            field=models.TextField(default=None, null=True),
        ),
    ]
