# Generated by Django 4.0.6 on 2022-08-11 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_messageroom_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageroom',
            name='student',
        ),
        migrations.RemoveField(
            model_name='messageroom',
            name='teacher',
        ),
        migrations.AddField(
            model_name='messageroom',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]