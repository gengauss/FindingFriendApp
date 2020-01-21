# Generated by Django 3.0 on 2020-01-20 02:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_auto_20200120_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='customers.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(default=uuid.UUID('b23a5bbd-2cfe-42a5-973a-ea4abf77a6b7'))),
                ('messages', models.ManyToManyField(blank=True, to='chat.Message')),
                ('participants', models.ManyToManyField(related_name='channel', to='customers.Customer')),
            ],
        ),
    ]