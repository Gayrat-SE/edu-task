# Generated by Django 4.0.6 on 2022-08-11 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_last_activity'),
        ('chat', '0008_alter_messageroom_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.teacher'),
        ),
    ]
