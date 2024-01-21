# Generated by Django 4.2.5 on 2024-01-20 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DmsApp', '0002_organization_user_volunteer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='user',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='user',
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_name',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='vol_name',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]