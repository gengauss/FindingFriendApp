# Generated by Django 3.0 on 2020-01-20 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(default='1999-01-01')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='None', max_length=1)),
                ('nationality', models.CharField(default='None', max_length=50)),
                ('hobby', models.TextField(default='None')),
                ('favorite_book', models.TextField(default='None')),
                ('picture', models.ImageField(blank=True, default='profile_image/default.png', null=True, upload_to='profile_image')),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='friendss',
            field=models.ManyToManyField(blank=True, related_name='users', to='customers.Friend'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
