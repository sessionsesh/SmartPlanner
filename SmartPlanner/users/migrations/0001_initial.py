# Generated by Django 3.1.1 on 2020-09-19 06:47

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
                ('registered', models.DateField(auto_now=True, verbose_name='registration_date')),
                ('last_update', models.DateField(auto_now_add=True, verbose_name='last_update')),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user account',
                'verbose_name_plural': 'user accounts',
                'unique_together': {('user', 'uuid')},
            },
        ),
    ]
