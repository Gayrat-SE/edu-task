# Generated by Django 4.0.6 on 2022-08-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_last_activity'),
        ('chat', '0011_alter_room_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='group', to='user.studentgroup'),
        ),
    ]